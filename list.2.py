fruits=["banana","apple","mango","papaya"]
fruits.append("orange")
print(fruits)
print()

fruits.append("cheery")
print(fruits)

fruits.insert(1,"mango")
print(fruits)


listA =["a","b","c","d"]
listB =["e","f","g","h"]
listA.extend(listB)
print(listA)

a=["p","r","a","j"]
a.extend("u")
print(a)
    
Fruits= ["grapes","banana","papaya","aplle","mango"]
del fruits[1]
print(fruits)
del fruits[2]
print(fruits)

fruits =["grapes","banana","papaya","apple","mango"]
fruits. pop()
print(fruits)

fruits=["grapes","banana","papaya","apple","mango"]
fruits.pop(2)
print(fruits)

fruits=["mango","grapes","banana","grapes","papaya","apple","mango"]
fruits.remove("mango")
print(fruits)
fruits.remove("grapes")
print(fruits)

num=[1,2,3,4,5,6,7]
print(num)
num.clear()
print(num)

listA=[33,22,66,88,11,55]
print(listA)
listA.sort()
print(listA)

listB = ["dip","adi","neel","swaraj","tanish"]
print(listB)
listB.sort()
print(listB)

listA=[33,22,66,88,11,77,55]
listB=["dip","adi","neel","swaraj","tanish"]
listA.sort(reverse=True)
print(listA)
listB.sort(reverse=True)
print(listB)
print('--------------')
ListA=[33,22,66,88,11,55]
listB=["dip","neel","tanish","swaraj","adi"]
new_listA = sorted(listA)
print(listA)
print(new_listA)
print('------------')
pair=[(x,y) for x in [1,2]for y in [3,4]]
print(pair)
print('--------------')
list1=[1,2]
list2['a','b']
pair2=[(x,y) x in list1 for y in list2]
print(pair2)
print('------')
num=[1,2,3,4,5]
square = [x*x for x in num]
print(square)

cube = [x*x*x for x in num]
print(cube)

names = ["dipanshu","neel","nitin"]

names_upper=[x.upper () for x in names]
print(names_upper)



