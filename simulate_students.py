def generate_students(num_students=100):
    import random
    INTERESTS = ["AI", "Security", "Data Science"]
    COURSES = ["CS101", "CS102", "AI201", "ML201", "Math101", "DS201", "Capstone"]
    students = []

    def ensure_valid_path(courses, graph):
        valid = []
        for c in courses:
            prereqs = list(graph.predecessors(c))
            if all(p in courses for p in prereqs):
                valid.append(c)
        return list(set(valid))

    from curriculum_graph import build_curriculum
    G = build_curriculum()

    for sid in range(num_students):
        sampled = random.sample(COURSES, random.randint(2, 4))
        completed = ensure_valid_path(sampled, G)
        grades = {c: round(random.uniform(2.0, 4.0), 2) for c in completed}
        gpa = round(sum(grades.values()) / len(grades), 2) if grades else 0.0
        interest = random.choice(INTERESTS)
        students.append({
            "student_id": sid,
            "completed_courses": completed,
            "grades": grades,
            "GPA": gpa,
            "interest": interest
        })
    return students
