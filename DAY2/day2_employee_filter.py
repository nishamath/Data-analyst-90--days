# Day 2: Employee Filtering using Loops and Conditions

# Basic condition
age = 20
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Dataset
employees = [
    {"name": "Anu", "age": 23, "salary": 40000},
    {"name": "Rahul", "age": 24, "salary": 34000},
    {"name": "Meena", "age": 20, "salary": 24000},
    {"name": "Arjun", "age": 21, "salary": 80000},
    {"name": "Diya", "age": 26, "salary": 60000}
]

# Filter employees with salary > 40000
salary_threshold = 40000

high_salary = []
for emp in employees:
    if emp["salary"] > salary_threshold:
        high_salary.append(emp["name"])

print("High salary employees:", high_salary)
print("Count:", len(high_salary))


# Employees with age < 25
print("Employees with age < 25:")
for emp in employees:
    if emp["age"] < 25:
        print(emp["name"])
