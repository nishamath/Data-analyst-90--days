# -----------------------------------------
# LOOPS + CONDITIONS PRACTICE
# -----------------------------------------

# Simple if-else condition

age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")


# -----------------------------------------
# Employee Dataset
# -----------------------------------------

employees = [
    {"name": "Anu", "age": 23, "salary": 40000},
    {"name": "Rahul", "age": 24, "salary": 34000},
    {"name": "Meena", "age": 20, "salary": 24000},
    {"name": "Arjun", "age": 21, "salary": 80000},
    {"name": "Diya", "age": 26, "salary": 60000}
]


# -----------------------------------------
# Find employees with salary > 40000
# -----------------------------------------

salary_limit = 40000

print("\nEmployees with salary greater than 40000:")

for emp in employees:
    if emp["salary"] > salary_limit:
        print(emp["name"])


# -----------------------------------------
# Store high salary employees in list
# -----------------------------------------

high_salary = []

for emp in employees:
    if emp["salary"] > 40000:
        high_salary.append(emp["name"])

print("\nHigh Salary Employees:", high_salary)


# -----------------------------------------
# List Comprehension (Professional Way)
# -----------------------------------------

high_salary_comp = [
    emp["name"]
    for emp in employees
    if emp["salary"] > 40000
]

print("\nUsing List Comprehension:", high_salary_comp)


# -----------------------------------------
# Find employees with age < 25
# -----------------------------------------

print("\nEmployees with age less than 25:")

for emp in employees:
    if emp["age"] < 25:
        print(emp["name"])


# -----------------------------------------
# Count high salary employees
# -----------------------------------------

count = 0

for emp in employees:
    if emp["salary"] > 40000:
        count += 1

print("\nNumber of High Salary Employees:", count)


# -----------------------------------------
# Another Professional Counting Method
# -----------------------------------------

high_salary_names = [
    emp["name"]
    for emp in employees
    if emp["salary"] > 40000
]

print("\nEmployees:", high_salary_names)
print("Count:", len(high_salary_names))


# -----------------------------------------
# Average Salary
# -----------------------------------------

total_salary = 0

for emp in employees:
    total_salary += emp["salary"]

average_salary = total_salary / len(employees)

print("\nAverage Salary:", average_salary)


# -----------------------------------------
# Highest Salary Employee
# -----------------------------------------

highest_salary_emp = employees[0]

for emp in employees:
    if emp["salary"] > highest_salary_emp["salary"]:
        highest_salary_emp = emp

print("\nHighest Salary Employee:")
print(highest_salary_emp["name"], "-", highest_salary_emp["salary"])


# -----------------------------------------
# Lowest Salary Employee
# -----------------------------------------

lowest_salary_emp = employees[0]

for emp in employees:
    if emp["salary"] < lowest_salary_emp["salary"]:
        lowest_salary_emp = emp

print("\nLowest Salary Employee:")
print(lowest_salary_emp["name"], "-", lowest_salary_emp["salary"])


# -----------------------------------------
# Employees age > 22
# -----------------------------------------

print("\nEmployees with age greater than 22:")

for emp in employees:
    if emp["age"] > 22:
        print(emp["name"])


# -----------------------------------------
# Total Salary Expense
# -----------------------------------------

total_expense = 0

for emp in employees:
    total_expense += emp["salary"]

print("\nTotal Salary Expense:", total_expense)
