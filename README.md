# AI Curriculum Planner – Adaptive Academic Advising Using Reinforcement Learning

This project simulates a university academic advising system using reinforcement learning (RL) and curriculum graph modeling. It generates personalized course recommendations for 100 students based on interests, GPA, and prerequisite constraints.

---

##  Features

- Curriculum modeled as a directed graph (courses & prerequisites)
- 100 simulated students with:
  - GPA, completed courses, and academic interests
- Course recommendation logic using a custom RL environment
- Term-wise simulation (max 6 terms)
- Retake policy for failed courses
- Graduation tracking
- Visual comparison between AI, Data Science, and Security students
- Full result logging + CSV/JSON outputs

---

##  How to Install & Run

### 1. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run simulations

```bash
python simulate_students.py
python run_rl_simulation.py
python visualize_graph.py
```

### 4. Explore notebook

```bash
jupyter notebook ai_curriculum_planner.ipynb
```

---

##  Sample Outputs

* `results/student_results.csv`: summary of each student (GPA, interest, courses taken)
* `results/term_logs.json`: per-term logs of decisions
* `results/curriculum_graph.png`: visual of curriculum structure

---

##  Dependencies

* Python 3.10+
* pandas
* numpy
* networkx
* matplotlib
* scikit-learn
* gym==0.26.2

---

##  License

MIT License
