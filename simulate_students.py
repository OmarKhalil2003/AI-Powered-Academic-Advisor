import random
import pandas as pd

def generate_students(num_students=100):
    INTERESTS = ["AI", "Security", "Data Science"]
    COURSES = ["CS101", "CS102", "AI201", "ML201", "Math101", "DS201", "Capstone"]
    students = []

    for sid in range(num_students):
        completed = random.sample(COURSES, random.randint(1, 4))
        grades = {c: round(random.uniform(2.0, 4.0), 2) for c in completed}
        gpa = round(sum(grades.values()) / len(grades), 2)
        interest = random.choice(INTERESTS)
        students.append({
            "student_id": sid,
            "completed_courses": list(set(completed)),
            "grades": grades,
            "GPA": gpa,
            "interest": interest
        })
    return students

if __name__ == "__main__":
    students = generate_students()
    df = pd.DataFrame(students)
    df.to_csv("results/student_data.csv", index=False)
