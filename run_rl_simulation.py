import pandas as pd
import random, json
from curriculum_graph import build_curriculum
from simulate_students import generate_students  
from curriculum_env import CurriculumEnv
import os

os.makedirs("results", exist_ok=True)

graph = build_curriculum()

students = generate_students()

results = []

term_logs = {}

for student in students:
    env = CurriculumEnv(student, graph)
    env.reset()
    log = []
    total_reward = 0

    for term in range(6): 
        eligible = env.get_eligible_courses()
        if not eligible:
            break
        selected = random.sample(eligible, min(3, len(eligible)))
        _, reward, done = env.step(selected)
        total_reward += reward
        log.append({
            "term": term + 1,
            "selected_courses": selected,
            "GPA": student["GPA"],
            "reward": round(reward, 2)
        })
        if done:
            break

    results.append({
        "student_id": student["student_id"],
        "interest": student["interest"],
        "final_GPA": student["GPA"],
        "total_courses": len(student["completed_courses"]),
        "graduated": "Capstone" in student["completed_courses"],
        "total_reward": round(total_reward, 2)
    })

    term_logs[student["student_id"]] = log

pd.DataFrame(results).to_csv("results/student_results.csv", index=False)

with open("results/term_logs.json", "w") as f:
    json.dump(term_logs, f, indent=2)

print("Simulation completed and results saved.")
