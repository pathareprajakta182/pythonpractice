# A tuple is a collection of items , just like a list , but with one important difference:
# Tuples are immutable (cannot be changed after creation)


listA = [10,20,30,40]         # list
print(listA)
listA[1]=44
print(listA)
print(type(listA))
print(30 in listA)

# tuple---------------


tupA = 11,
print(tupA)
print(type(tupA))

tupB = 11,22,33,44
print(tupB)
print(type(tupB))

tupC = ("dipanshu","chawde",11,True)
print(tupC)
print(type(tupC))

# does tuples stores the values  by index -------- yes

print(tupC[0])
print(tupC[3])
#tupC[1]="masalkar"     
#print(tupC)          # TypeError: tuple object does not support item assignment
# can we update 1 single value ? NO , fixed length
# tuples are fixed length

# why use tuple ?

# when data should not change (e.g.,coordinates , constants)
#  faster than lists
# safe from accidental modification

# particular value exits in tuple

tupC = ("dipanshu","chawde",11,True,"pune")
print("dipanshu" in tupC)
print("Dipanshu" in tupC)

# length of tuple---------

print(len(listA))

print(len(tupC))

tupD = [111,5,78,45,32,49,875,10,32]
print(max(tupD))
print(min(tupD))

print(type([1,2,3,4,5]))
print(type((1,2,3,4,5)))

# packing and unpacking--------

tupE = (11,22,33,44)      # packing
print(tupE)

a,b,c,d=tupE              # unpacking
print(a)
print(b)
print(c)
print(d)


tupF = (11,22,55,77,88)
p,q,r,s,t= tupF
print(p)
print(q)


# looping-------------

tupF =(11,22,33,44,55,66)
for x in range(len(tupF)):
   # print(x)
    print(tupF[x])

tupG = ("a","b","c","d","e","f")
i = 0
while(i<len(tupG)):
    print(tupG[i])
    i=i+1



# count----- counts number of coourence of element

tupG=("a","b","c","d","e","f","f","a","e","a")
print(tupG.count("e"))
print(tupG.count("a"))
print(tupG.count("z"))

# index finds of index of element-------


print(tupG.index("a"))
print(tupG.index("e"))
print(tupG.index("z"))   # valueerror:


# single element tuple (Important)

t = (5,)    # correct

t=(5)       # wrong----becomes int


# key characteristics-------

# - ordered (items keep their position)
# - Immutable (can not modify , add ,or remove items)
# - Allows duplicate values
# - Can store different data types