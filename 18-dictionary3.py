# dict.fromkeys() - is used to create a new dictionary using:
# * A sequence of keys
# * one default value for all keys

# syntax
    # dict. fromkeys(keys, default_ value)
        # * keys - list / tumple / string / set (any interable)
        # * default_value - value assigned to all keys
        # (default is None if not provided)


# Creating dictionay with keys only

keys= ["name","age","rollno","class"]
d= dict.fromkeys(keys)
print(d)

d["name"]="dipanshu"
print(d)

# creating dictionary with keys only and default value "unknown"

d2= dict.fromkeys(keys,"unknown")
print(d2)

d2["name"] ="neel"
print(d2)

# Using string as a keys (Every character becomes a key!)

d3=dict.fromkeys("abc",1)
print(d3)

# important : If you use a mutable value like a list, all keys share the SAME list.

d4= dict.fromkeys(["x","y"],[])
print(d4)

d4["x"].append(1)
print(d4)

d4["y"].append(2)
print(d4)

d4["x"]="nill" 
print(d4)

d4["y"]="dipanshu" 
print(d4)

#-------------------------------------------------------

#copy

student1 ={
    "name":"rajasi",
    "class":"5A"

}

student2 = student1

print(student1)
print(student2)

student2["name"]="neel"
print(student2)

student1["class"]="4A"
print(student1)
print(student2)


#copy()

student= {
    "name":"rajasi",
    "class":"5A"

}

new_student=student.copy()
print(student)
print(new_student)

student["name"]="neel"
print(student)
print(new_student)



new_student["class"]="5B"
print(student)
print(new_student)







        
