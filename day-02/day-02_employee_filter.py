# LOOPS + CONDITIONS

age=20
if age>=18:
    print("Adult")
else:
    print("Minor")


employees=[
    {"name":"Anu","age":23,"salary":40000},
    {"name":"Rahul","age":24,"salary":34000},
    {"name":"Meena","age":20,"salary":24000},
    {"name":"Arjun","age":21,"salary":80000},
    {"name":"Diya","age":26,"salary":60000} 
]

# Find employees with salary>40000
salary_N=40000
for emp in employees:
    if emp["salary"]>salary_N:
        print(emp["name"])
# -----------------------------------------------

# high_salary=[]
for emp in employees:
    if emp["salary"]>40000:
        high_salary.append(emp["name"])
print(high_salary)
# -------------------------------------------------------


# LIST COMPREHENSION (PROFESSIONAL WAY)




# Find employees with age <25

for emp in employees:
    if emp["age"]<25:
        print(emp["name"])

# Number of high salary employees
for emp in employees:
    if emp['salary']>40000:
        print(len('salary'))     #   WRONG (salary is just a word(string))   --Length of 'salary'=6
# so it will always print 6,not count employees


# CORRECT WAY 


count=0
for emp in employees:
    if emp['salary']>40000:
        count+=1
print("High salary employees:",count)
# --------------------------------------------------------------------

high_salary=[]
for emp in employees:
    if emp['salary']>40000:
        high_salary.append(emp['name'])
print("Employees:",high_salary)
print("Count:",len(high_salary))
