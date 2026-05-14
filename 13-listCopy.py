num1=[11,22,33,44]
num2=num1
print(num1)
print(num2)

num1[1]=777
print(num1)
print(num2)

num2[3]=100
print(num1)
print(num2)

# copy----------------

listA=["a","b","c","d","e"]
listB=listA.copy()
print(listA)
print(listB)
print("---------------")

listA[2]=11
print(listA)
print(listB)

listB[3]=44
print(listA)
print(listB)
      
      