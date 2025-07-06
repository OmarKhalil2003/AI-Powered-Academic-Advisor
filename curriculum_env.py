class CurriculumEnv:
    def __init__(self, student, graph):
        import random
        self.random = random
        self.graph = graph
        self.student = student
        self.all_courses = list(graph.nodes)
        self.max_courses = 5
        self.term = 0
        self.reset()

    def _get_state(self):
        completed = set(self.student["completed_courses"])
        course_vector = [1 if c in completed else 0 for c in self.all_courses]
        interest_vector = [int(self.student["interest"] == i) for i in ["AI", "Security", "Data Science"]]
        gpa_scaled = [self.student["GPA"] / 4.0]
        return course_vector + interest_vector + gpa_scaled

    def reset(self):
        self.term = 0
        self.state = self._get_state()
        return self.state

    def is_course_eligible(self, course):
        completed = set(self.student["completed_courses"])
        prereqs = list(self.graph.predecessors(course))
        return all(p in completed for p in prereqs) and course not in completed

    def get_eligible_courses(self):
        return [c for c in self.all_courses if self.is_course_eligible(c)]

    def step(self, selected_courses):
        reward = 0
        completed = self.student["completed_courses"]
        grades = self.student["grades"]
        self.term += 1

        for course in selected_courses:
            if self.is_course_eligible(course):
                grade = self.random.uniform(2.5, 4.0)
                grades.setdefault(course, grade)
                if course not in completed:
                    completed.append(course)
                reward += (grade - 2.5)
                if self.student["interest"][:2] in course:
                    reward += 0.5

        self.student["GPA"] = round(sum(grades.values()) / len(grades), 2)
        done = self.check_graduation()
        return self._get_state(), reward, done

    def check_graduation(self):
        required = ["CS101", "CS102", "Math101", "DS201", "Capstone"]
        return all(r in self.student["completed_courses"] for r in required) and self.term <= 6

