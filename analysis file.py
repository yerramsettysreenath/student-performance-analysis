import pandas as pd

# Load dataset
df = pd.read_csv("students data.csv")

# Show first rows
print("Dataset Preview:")
print(df.head())

# Basic Analysis
print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

# Top performer
top_student = df.loc[df["Marks"].idxmax()]
print("\nTop Performer:")
print(top_student)

# Attendance vs Marks
print("\nCorrelation between Attendance and Marks:")
print(df["Attendance"].corr(df["Marks"]))