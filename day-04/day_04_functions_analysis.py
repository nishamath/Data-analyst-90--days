# -----------------------------------------
# BASIC FUNCTION
# -----------------------------------------

def greet():
    print("Hello")

greet()


# -----------------------------------------
# FUNCTION WITH PARAMETER
# -----------------------------------------

def print_name(name):
    print(name)

print_name("NISHA")


# -----------------------------------------
# FUNCTION WITH RETURN
# -----------------------------------------

def add(a, b):
    return a + b

result = add(10, 5)

print("Addition:", result)


# -----------------------------------------
# EMPLOYEE DATA
# -----------------------------------------

employees = [
    {"name": "Anu", "age": 23, "salary": 80000},
    {"name": "Rahul", "age": 24, "salary": 34000},
    {"name": "Meena", "age": 20, "salary": 24000},
    {"name": "Arjun", "age": 21, "salary": 80000},
    {"name": "Diya", "age": 26, "salary": 60000}
]


# -----------------------------------------
# FUNCTION - AVERAGE SALARY
# -----------------------------------------

def get_avg_salary(employees):

    total = 0

    for emp in employees:
        total += emp["salary"]

    return total / len(employees)


avg_salary = get_avg_salary(employees)

print("\nAverage Salary:", avg_salary)


# -----------------------------------------
# ABOVE AVERAGE EMPLOYEES
# -----------------------------------------

def get_above_avg(employees, avg_salary):

    result = []

    for emp in employees:
        if emp["salary"] > avg_salary:
            result.append(emp["name"])

    return result


above = get_above_avg(employees, avg_salary)

print("\nEmployees Above Average Salary:", above)


# -----------------------------------------
# HIGHEST SALARY EMPLOYEE
# -----------------------------------------

def get_highest_employee(employees):

    return max(employees, key=lambda x: x["salary"])


highest = get_highest_employee(employees)

print("\nHighest Salary Employee:")
print(highest)


# -----------------------------------------
# LOWEST SALARY EMPLOYEE
# -----------------------------------------

def get_lowest_employee(employees):

    return min(employees, key=lambda x: x["salary"])


lowest = get_lowest_employee(employees)

print("\nLowest Salary Employee:")
print(lowest)


# -----------------------------------------
# TOTAL SALARY EXPENSE
# -----------------------------------------

def get_total_salary(employees):

    total = 0

    for emp in employees:
        total += emp["salary"]

    return total


total_salary = get_total_salary(employees)

print("\nTotal Salary Expense:", total_salary)


# -----------------------------------------
# EMPLOYEES AGE GREATER THAN 22
# -----------------------------------------

def get_age_above_22(employees):

    result = []

    for emp in employees:
        if emp["age"] > 22:
            result.append(emp["name"])

    return result


age_above_22 = get_age_above_22(employees)

print("\nEmployees Age > 22:", age_above_22)
