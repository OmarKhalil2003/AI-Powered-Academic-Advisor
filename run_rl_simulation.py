import pandas as pd
import json
from curriculum_graph import build_curriculum
from simulate_students import generate_students
from curriculum_env import CurriculumEnv

G = build_curriculum()
students = generate_students()
results, term_logs = [], {}

for student in students:
    env = CurriculumEnv(student, G)
    env.reset()
    log = []
    total_reward = 0

    for _ in range(6):
        eligible = env.get_eligible_courses()
        if not eligible:
            break
        selected = env.random.sample(eligible, min(3, len(eligible)))
        _, reward, done = env.step(selected)
        total_reward += reward
        log.append({
            "term": env.term,
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
        "graduated": env.check_graduation(),
        "total_reward": round(total_reward, 2)
    })
    term_logs[student["student_id"]] = log

pd.DataFrame(results).to_csv("results/student_results.csv", index=False)
with open("results/term_logs.json", "w") as f:
    json.dump(term_logs, f, indent=2)
