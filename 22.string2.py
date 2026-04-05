# upper,lower, capitalize , count , find ,index , endswith , startswith 
# isLower () , isUpper ()
print("some changes")
print("hello".upper())
print("Hello".lower())
print("hello".capitalize())

a="nitin"
print(a.count("t"))
print(a.count("i"))

# startswith----------------

b="dipanshu"
print(b.startswith("d"))
print(b.startswith("dip"))
print(b.startswith("D"))
print(b.startswith("Dip"))

#endswith-----------------

b = "dipanshu"
print(b.endswith('u'))
print(b.endswith("shu"))
print(b.endswith("U"))
print(b.endswith("SHU"))

# find = return index of first matching ch, if not found matching ch returns -1

c = 'tanish'
res= c.find("a")
print(res)


print(c.find("tan"))
print(c.find("taa"))

c = "nitin"
print(c.find("i"))

# index-----------------

d = "dipanshu"
print(d.index("i"))
print(d.index("n"))
#print(d.index("x"))

c = "nitin"
print(c.index("n"))
print(c.index("i"))

name ="neel"
print(name.islower())
print(name.isupper())


name= "12s3"
print(name.isalpha())
print(name.isnumeric())
print(name.isalnum())

# isspace------------

print("   ".isspace())
print(" a".isspace())

# istitle-------------

x = " My Name Is Dipanshu"
print(x.title())
print(x.istitle())

# join-----------------

info = ["dipanshu","chawde","9076404532"]
print("@".join(info))

print("123".join(info))

info = ["prajakta","pathare"]
print("narayan".join(info))



    