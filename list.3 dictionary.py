#Descriptive datatype
#dictionary in python
#key value

 dictA={
    "fname":"dipanshu",
    "lname":"chawde",
    "age":42,
    "rollno":23

    }
print(dictA)
print(type(dictA))

print('----------')

vehicle={
    "coloue":"red",
    "type":"SUV"

}
print(vehicle)
print(vehicle["coloue"])
print(vehicle["type"])

print("-------------------------")
#CRUD operations , loops


student={
    "fname":"neel",
    "lname":"chawde",
    "age":10,
    "rollno":12

}
print(student)
print(student["fname"])
print(student["lname"])

print(student["age"])
print(student["rollno"])

print("age" in student)
print("class" in student)

print(student.get("fname"))
print (student.get("lname"))
print(student.get("rollno"))

print(student.keys())
print(student.values())
print(student.items())

print(student.keys(), student.values())

print("--------------------------------")
# add / update----------------

student={
    "fname":"neel",
    "lname":"chawde",
    "age":10,
    "rollno":"23"
}

print(student)
student["class"]="3B"
print(student)

student["class"]="4A"
print(student)

# using update method

student.update({"language":"marathi"})
print(student)

student.update({"language":"english"})
print(student)

# delete---------------------
# delete any key 


#del

print(student)

del student["language"]
print(student)

#pop()

print(student)
dval = student.pop("class")
print(student)

#popitem()= last key deletes

student={
    "fname":"nell",
    "lname":"chawde",
    "age":10,
    "rollno":12
}
print(student)
student.popitem()
print(student)

#clear()=remove all key
student.clear()
print(student)


print('----------------------')

batch={
    "sec":"A",
    "total":20
}

batch.pop("age",None)
print(batch)
