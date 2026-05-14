employees = [
    {"id":1 , "name":"John" , "age": 28 , "salary":45000 , "department":"IT"},
    {"id":2 , "name":"Alice" , "age": 34 , "salary":72000 , "department":"HR"},
    {"id":3 , "name":"Bob" , "age": 25 , "salary":38000 , "department":"IT"},
    {"id":4 , "name":"David" , "age": 42 , "salary":96000 , "department":"finance"},
    {"id":5 , "name":"Sara" , "age": 30 , "salary":55000 , "department":"HR"},

]

# extract name of all employees

for x in employees:
    print(x['name'])

print("--------------------------------------------------------------")

nms = [ x['name']for x in employees]
print(nms)

print('-----------------------------------')

print(list(map(lambda x:x['name'],employees)))
print(nms)

print("----------------------------")
print(list(map(lambda x : x['name'],employees)))

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# print increase salary of every employee by 10% ----- using map
# return list of increase salary do not change in the original dict

# 45000*1.10  ===[]
print(list(map(lambda emp :emp["salary"]*1.10,employees)))
print(employees)

# -----------------------------------------------------------

# for emp in employees
# ---------------------------------------------------------------------
# **kwargs
# emp = {"id":1 , "name":"John" , "age": 28 , "salary":45000 , "department":"IT"},
updated_employees = list(map(lambda emp:{**emp,"salary":emp['salary'] *1.10},employees))
print(updated_employees)

print("--------------------------")
# ----------------------------------------------------------------------
# Employees where salary greater then 50k
print(list(filter(lambda emp :emp['salary']>50000,employees)))

salaryabove50k = list(filter(lambda emp :emp['salary']>50000,employees))
print(salaryabove50k)

# --------------------------------------------------------------
print("-------------------------")
print(list(filter(lambda emp: emp["department"]=='IT',employees)))


# ----------------------------------------------------
# find max number

numbers = [67,87,5,90,76,99,34]
# max =employees[0]
max =0

for x in numbers:
    if x > max:
        max =x             # max = 0,67,87,87,90,90,99
print(max)

print("---------------------------------------------")

# finf max salary employees

max_sal_emp = employees[0]

print(max_sal_emp)
#{"id":1 , "name":"John" , "age": 28 , "salary":45000 , "department":"IT"},
#{"id":2 , "name":"Alice" , "age": 34 , "salary":72000 , "department":"HR"},
#{"id":3 , "name":"Bob" , "age": 25 , "salary":38000 , "department":"IT"},
#{"id":4 , "name":"David" , "age": 42 , "salary":96000 , "department":"finance"},
#{"id":5 , "name":"Sara" , "age": 30 , "salary":55000 , "department":"HR"},

for emp in employees:
    if emp['salary']>max_sal_emp['salary']:
        max_sal_emp = emp
print(max_sal_emp)

# find employees of age age >30

# ----------------------------------------------------------------------

# count total number of employees of hr dept

from functools import reduce

print(reduce(lambda total ,emp:total+(emp['department']=='IT'),employees,0))

# other way

count = sum(emp['department']=='HR' for emp in employees )
print(count)

# other way

highest = max(employees, key=lambda emp: emp["salary"])
print(highest)
