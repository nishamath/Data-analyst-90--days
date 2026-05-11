# -----------------------------------------
# Day 5 - KPI & Performance Analysis
# -----------------------------------------

employees = [
    {"name": "Anu", "salary": 80000, "kpi": 90},
    {"name": "Rahul", "salary": 34000, "kpi": 65},
    {"name": "Meena", "salary": 24000, "kpi": 55},
    {"name": "Arjun", "salary": 50000, "kpi": 95},
    {"name": "Diya", "salary": 60000, "kpi": 72}
]


# -----------------------------------------
# FUNCTION - Average KPI
# -----------------------------------------

def get_avg_kpi(employees):

    total = 0

    for emp in employees:
        total += emp["kpi"]

    return total / len(employees)


avg_kpi = get_avg_kpi(employees)

print("Average KPI:", avg_kpi)


# -----------------------------------------
# HIGH KPI EMPLOYEES
# -----------------------------------------

def get_high_kpi_employees(employees, avg_kpi):

    result = []

    for emp in employees:

        if emp["kpi"] > avg_kpi:
            result.append(emp["name"])

    return result


high_kpi = get_high_kpi_employees(employees, avg_kpi)

print("\nEmployees Above Average KPI:", high_kpi)


# -----------------------------------------
# TOP KPI EMPLOYEE
# -----------------------------------------

def get_top_employee(employees):

    return max(employees, key=lambda x: x["kpi"])


top_employee = get_top_employee(employees)

print("\nTop Performer:", top_employee["name"])
print("KPI Score:", top_employee["kpi"])


# -----------------------------------------
# AVERAGE SALARY
# -----------------------------------------

def get_avg_salary(employees):

    total = 0

    for emp in employees:
        total += emp["salary"]

    return total / len(employees)


avg_salary = get_avg_salary(employees)

print("\nAverage Salary:", avg_salary)


# -----------------------------------------
# HIGH SALARY BUT LOW KPI
# -----------------------------------------

def high_sal_low_kpi(employees, avg_salary, avg_kpi):

    result = []

    for emp in employees:

        if emp["salary"] > avg_salary and emp["kpi"] < avg_kpi:
            result.append(emp["name"])

    return result


special_case = high_sal_low_kpi(employees, avg_salary, avg_kpi)

print("\nHigh Salary but Low KPI:", special_case)


# -----------------------------------------
# LOW KPI EMPLOYEES
# -----------------------------------------

def get_low_kpi_employees(employees, avg_kpi):

    result = []

    for emp in employees:

        if emp["kpi"] < avg_kpi:
            result.append(emp["name"])

    return result


low_kpi = get_low_kpi_employees(employees, avg_kpi)

print("\nEmployees Below Average KPI:", low_kpi)


# -----------------------------------------
# TOTAL COMPANY SALARY EXPENSE
# -----------------------------------------

def get_total_salary(employees):

    total = 0

    for emp in employees:
        total += emp["salary"]

    return total


total_salary = get_total_salary(employees)

print("\nTotal Salary Expense:", total_salary)
