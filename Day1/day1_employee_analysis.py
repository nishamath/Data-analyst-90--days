# Day 1: Employee Analysis using Python

# Basic variables
name = "Nisha"
age = 25
salary = 50000.0
is_working = True

print(name)
print(age)
print(salary)
print(is_working)

# Dataset
employees = [
    {"name": "Anu", "age": 23, "salary": 20000},
    {"name": "Rahul", "age": 30, "salary": 50000},
    {"name": "Meena", "age": 26, "salary": 30000},
    {"name": "Divya", "age": 24, "salary": 70000},
    {"name": "Remiya", "age": 20, "salary": 50000}
]

# 1) Total employees
total = len(employees)

# 2) Average Salary
total_salary = 0
for emp in employees:
    total_salary += emp["salary"]

avg_salary = total_salary / total

# 3) Highest Salary Person
max_salary = 0
highest_name = ""
highest_age = 0

for emp in employees:
    if emp["salary"] > max_salary:
        max_salary = emp["salary"]
        highest_name = emp["name"]
        highest_age = emp["age"]

# 4) Youngest Person
min_age = 100
youngest_name = ""

for emp in employees:
    if emp["age"] < min_age:
        min_age = emp["age"]
        youngest_name = emp["name"]

# Final Output
print("Total employees:", total)
print("Average Salary:", avg_salary)
print("Highest Salary person:", highest_name)
print("Youngest Person:", youngest_name)
