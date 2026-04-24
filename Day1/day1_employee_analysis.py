##Basic python ##

# name="Nisha"
# age=25
# salary=50000.0
# is_working=True

# Print(name)
# Print(age)
# print(salary)
# print(is_working)


## create dataset ##
employees=[
    {"name":"Anu","age":23,"salary":20000},
    {"name":"Rahul","age":30,"salary":50000},
    {"name":"Meena","age":26,"salary":30000},
    {"name":"Divya","age":24,"salary":70000},
    {"name":"Remiya","age":20,"salary":50000}

]

# print(employees)


# Analysis (CORE TASK)

# Write code to find:
# 1) Total employees
# 2)Average Salary
# 3)Highest Salary Person
# 4)Youngest Person

# # 1)
for emp in employees:
    total=len(employees)
print(total)

# # # 2)
total_salary=0
for emp in employees:
    total_salary= total_salary + emp['salary']
    avg_salary=total_salary/total
print(avg_salary)


# 3)

total=len(employees)
total_salary= 0
for emp in employees:
    total_salary=total_salary+emp["salary"]
avg_Salry=total_salary/total_salary
print(total_salary)

# 4) Highest Salary Person
max_Salary=0
highest_name=" "
age=''

for emp in employees:
    if emp['salary']>max_Salary:
        max_Salary=emp["salary"]
        highest_name=emp["name"]
        age=emp['age']
print(max_Salary)
print(highest_name)
print(age)



# 4)Youngest Person

min_age=100
youngest_name=""

for emp in employees:
    if emp["age"]<min_age:
        min_age=emp["age"]
        youngest_name=emp["name"]
print(min_age)
print(youngest_name)





# FINAL print


# print("Total employees:",total)
# print("Average Salary:",avg_salary)
# print("Highest Salary person:",highest_name)
# print("Youngest Person:",youngest_name)
