students = [
    {
        "firstName":"neel",
        "lastName":"nitin",
        "age":"36",
        "skills":["python","sql"],
        "marks":{"maths":95,"science":97,"english":77}
            
        
    },
    {
    "firstName":"virat",
    "lastName":"koholi",
    "age":37,
    "skills":["python","sql","c"],
    "marks":{"maths":95,"science":92,"english":70}
    },
    {
    "firstName":"anand",
    "lastName":"raj",
    "age":35,
    "skills":["python","sql","diango"],
    "marks":{"maths":55,"science":92,"english":75}

    },
    {
        "firstName":"kavita",
        "lastName":"godbole",
        "age":32,
        "skills":["python"],
        "marks":{"maths":92,"science":44,"english":76}

    }
]

num = [10,20,30,40]

names= ["dipanshu","nitin","tanish","neel"]

print(names[0])
print(names[0])
print(students[0])

# ---------------------------------------------------------------------

# print names of students

for x in students:
    print(x['firstName'])

# --------------------------------------------------------------

# print name and total marks of each students

# x = {
# "firstName":"neel",
# "lastName":"nitin",
# "age":36,
# "skills":["python","sql"],
# "marks":{"maths":95,"sceince":97,"english":77}
# }

for x in students:
    total = x ['marks']['maths']+x['marks']['science']+x['marks']['english']
    print(f"{x['firstName']}:{total}")

# -------------------------------------------------------------------------

# print name and numbers of skills each students have

for x in students:
    length = len (x['skills'])
    print(f"{x['firstName']}:skills{length}")

    print('---------------------------')
    
    # --------------------------------------------------------

    # lsi comprehension

    # print names of students

    name_list = [x['firstName']for x in students]
    print(name_list)

    print([x["firstName"]for x in students])

    # ------------------------------------------------------

    # print name and total marks of each students

    result = [(x["firstName"],x['marks']['maths']+x['marks']['science']+x['marks']['english']) for x in students]
    print(result)

    print(type(result[0]))