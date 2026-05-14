# operation with every element
# find age

birthYear =[2021,2000,1986,1999,2015,2008,2025]

age=[]

for yr in birthYear:
    age.append(2026-yr)      # 2021,2000,1986............
print(age)

# -------------MAP Functions---------------------------

ag = map(lambda x:2026-x,birthYear)
print(ag)

# map ()returns a map object (interator)
# python does not show the actual values until you iterate or convert it

final_age = list(ag)

# extracts all values from the map object,stores them in a list
# After this,the map object is exhausted (cannot be reused)

print(final_age)
print(final_age)

# print(list(ag))

# list comprehensions---------------------

age2 =[2026-x for x in birthYear]
print(age2)

print("-----------------------------------------------")
#---------------------------------------------------------------------

# filter element

marks =[90,76,88,23,11,56,45,35]
passM=[]
failM=[]

for mk in marks:
    if mk >=35:
        passM.append(mk)

    else:
        failM.append(mk)
print(passM)
print(failM)

print("----------------------------------")

# filter

pass_marks_obj= filter(lambda x:x>=35,marks)
print(pass_marks_obj)

pass_marks_=list(pass_marks_obj)
pass_marks2=list(filter(lambda x:x>=35,marks))

print(pass_marks2)


fail_marks_obj =filter(lambda x:x<35,marks)
print(fail_marks_obj)

fail_marks=list(fail_marks_obj)
print(fail_marks)

print("-----------------------------------")

# list comprehensions--------------------

failM=[x for x in marks if x<35]
print(failM)

passM=[x for x in marks if x>=35]
print(passM)

#-------------------------------------------

# amount deposit withdraw

# filter-----------

transactions = [100,200,1000,-40,-250,99,-700,44,500]

deposit = list (filter(lambda x: x>0,transactions))
withdraw = list(filter(lambda x:x<0,transactions))
print(f"deposit={deposit}")
print(f"withdraw={withdraw}")

print("---------------------------------")

# sum of all elements

nums = [22,66,88,99,55,66,99,33,11]
# total=0
# for x in nums:
# total = total +x
# print(total)

# reduce

from functools import reduce
total = reduce(lambda total , x:total+x , nums,0)
print(total)