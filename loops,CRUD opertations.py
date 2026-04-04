names=["nitin","dipanshu","neel","tanish"]

# for

for x in range(len(names)):
     print(names[x])

# while 

while(x<len(names)):
     print(names[x])
     x=x+1

# append, insert, extend

fruits=["banana","mango","papaya","apple","grapes"]

fruits.append("orange")
print(fruits)

x=[1.2]
y=[2,3]
x.append(y)
print(x)


a=["p","r","a"]
a.extend("ju")
print(a)
# insert------------------
fruits=["grapes","banana","mango","apple","papaya"]

fruits.insert(1,"kiwi")
print(fruits)

fruits.insert(0,"orange")
print(fruits)

fruits.insert(len(fruits),"strawberry")
print(fruits)

# extend-----------------

listA=["a","b","c","d"]
listB=["e","f","g","h"]


listA.extend(listB)
print(listA)
print(listB)

a=["s","w","a"]
a.extend("raj")
print(a)


# deleting element in list------------------


fruits=["grapes","banana","mango","apple","papaya"]
del fruits[3]
print(fruits)


fruits=["grapes","banana","mango","apple","papaya"]
fruits.pop()
print(fruits)

fruits.pop()
print(fruits)

fruits=["grapes","banana","mango","apple","papaya"]
fruits.pop(2)
print(fruits)

# remove value------------------

fruits=["grapes","banana","mango","apple","papaya"]
fruits.remove("apple")
print("fruits")

fruits.remove("grapes")
print(fruits)

#fruits.remove("kiwi")
#print(fruits)

# clear----------- delete all elements

num=[1,2,3,4,5,6,]
print(num)
num.clear()
print(num)


print("--------------------------")



fruits=["grapes","banana","mango","apple","papaya"]
print(fruits)
#fruits.clear()
#print(fruits)

#fruits . append("kiwi")
#print(fruits)
#fruits . append("cherry")
#print(fruits)
#fruits.insert(0,"watermelon")
#print(fruits)

#a#= [1,2,3,4,]
#b=[4,5,7,8,]
#b.extend(a)
##print(a)
#print(b)

fruits=["banana","mango","orange","cherry"]

#del fruits [0]
#print(fruits)

#fruits.pop()
#print(fruits)    

#f#ruits.pop(1)
#print(fruits)

#fruits.remove("cherry")
#print(fruits)

fruits.clear()
print(fruits)
