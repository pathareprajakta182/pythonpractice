keys=["name","age","rollno","class"]

d=dict.fromkeys(keys)
print(d)

d["name"]="neel"
print(d)

d2=dict.fromkeys(keys,"unknown")
print(d2)

d2["name"]="dipanshu"
print(d2)

d2["name"]="praju"
print(d2)

d3=dict.fromkeys("abc",0)
print(d3)

d4=dict.fromkeys(["x","y"],[])
print(d4)

d4["x"].append(1)
print(d4)

d4["y"].append(2)
print(d4)

d4["y"]="nill"
print(d4)

d4["x"]="rajasi"
print(d4)



student1={
    "name":"rajasi",
    "class":"5A"

}

student2 = student1


print(student1)
print(student2)

student1["class"]="4A"
print(student1)
print(student2)

student={
    "name":"rajasi",
    "class":"5A"

}

new_student=student.copy()
print(student)
print(new_student)

student["name"]="nill"
print(student)
print(new_student)


new_student["class"]="5B"
print(student)
print(new_student)
