info = {
    "fname":"dipanshu",
    "lname":"chawade",
    "age":42,
    "rollno":34

}

a = info.get("fname")
print(a)
b = info.get("lname")
print(b)

info["class"]="python"
print(info)

info["class"]="javascript"
print(info)

info.update({"location":"pune"})
print(info)

info.update({"location":"mumbai"})
print(info)

del info["location"]
print(info)

info.pop("rollno")
print(info)

info.popitem()
print(info)

info.clear()
print(info)

info = {
    "fname":"dipanshu",
    "lname":"chawde",
    "age":42,
    "rollno":23

}

print(info.keys())
print(info.values())
print(info.items())

# looping------------------------------------

for v in info. values():
    print(v)

for k in info. keys():
    print(k)

for i in info.items():
    print(i)


for k, v in info.items():
    print(f'keys :{k}  values :{v}')


# set default-----------------------------------------------

info = {
    "fname": "dipanshu",
    "lname":"chawde",
    "age": 42,
    "rollno":23
}

info["location"]= "pune"

s1 = info.setdefault("location","mumbai")
print(info)
print(s1)

s2= info.setdefault("language", "marathi" )
print(info)
print(s2)

info.setdefault("skills",[]).append("python")
print(info)

info.setdefault("skills",[]).append("javascript")
print(info)