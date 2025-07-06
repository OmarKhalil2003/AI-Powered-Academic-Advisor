import pandas as pd

df = pd.read_csv("results/student_results.csv")
print("Graduation Rate:", df['graduated'].mean())
print("Average GPA:", df['final_GPA'].mean())
print("Most Popular Courses: Coming soon...")
