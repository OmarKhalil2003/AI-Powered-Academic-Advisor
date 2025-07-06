import numpy as np

INTEREST_MAP = {
    "AI": ["AI201", "ML201"],
    "Data Science": ["DS201"],
    "Security": ["CS102"]
}

def is_graduated(student):
    required = {"CS101", "CS102", "Math101", "DS201", "Capstone"}
    return all(r in student["completed_courses"] for r in required) and student["GPA"] >= 2.5

def get_failed_courses(student):
    return [c for c, g in student["grades"].items() if g < 2.0]

class CurriculumEnv:
    def __init__(self, student, graph):
        self.graph = graph
        self.student = student
        self.all_courses = list(graph.nodes)
        self.max_courses = 5
        self.reset()

    def _get_state(self):
        completed = set(self.student["completed_courses"])
        course_vector = [1 if c in completed else 0 for c in self.all_courses]
        interest_vector = [int(self.student["interest"] == k) for k in INTEREST_MAP]
        gpa_scaled = [self.student["GPA"] / 4.0]
        return np.array(course_vector + interest_vector + gpa_scaled)

    def reset(self):
        self.state = self._get_state()
        return self.state

    def get_eligible_courses(self):
        completed = set(self.student["completed_courses"])
        eligible = []
        for course in self.all_courses:
            if course not in completed:
                prereqs = list(self.graph.predecessors(course))
                if all(p in completed for p in prereqs):
                    eligible.append(course)
        return eligible + get_failed_courses(self.student)

    def step(self, selected_courses):
        reward = 0
        for course in selected_courses:
            if course in self.get_eligible_courses():
                grade = np.random.uniform(2.5, 4.0)
                self.student["grades"][course] = grade
                if course not in self.student["completed_courses"]:
                    self.student["completed_courses"].append(course)
                reward += (grade - 2.5)
                if course in INTEREST_MAP[self.student["interest"]]:
                    reward += 0.5
        self.student["GPA"] = round(sum(self.student["grades"].values()) / len(self.student["grades"]), 2)
        self.state = self._get_state()
        return self.state, reward, is_graduated(self.student)
