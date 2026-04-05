setA = {11,22,33,44}
setB = {11,33,55,66,77}
setC = setA.intersection(setB)
print(setC)

print("--------------------------")

setA ={11,22,33,44}
setB ={11,33,55,66,77}
setA.intersection_update(setB)
print(setA)
print(setB)

print("------------------")

setA = {"a","b","c",11,33}
setB = {11,33,55,66,77}
setD = setB.difference(setA)
print(setD)

print('-------------------------')
  
setA = {"a","b","c",11,33}
setB = {11,33,55,66,77}
setD.difference_update(setB)
print(setA)

print("--------------------")

setA = {"a","b","c",11,33}
setB = {11,33,55,66,77}
setF = setA.symmetric_difference(setB)
print(setF)

print("-----------------")


setA = {"a","b","c",11,33}
setB = {11,33,55,66,77}
setA.symmetric_difference_update(setB)
print(setA)
print(setB)

print("-------------------")
setA = {"a","b","c"}
setB = {11,33,55,66,77}
print(setA.isdisjoint(setB))  

print("-------------------")

setA = {"a","b","c",11,33,55,66,77}
setB = {11,33,55,66,77}
print(setB.issuperset(setA))
print(setA.issuperset(setB))
print(setB.issubset(setA))

print("--------------")

setA = {"a","b","c",11,33}
setB = {1,2,3,4,5,}
print(setA.union(setB))

print("--------------------")

setA = {"a","b","c",11,33}
setA.discard("a")
print(setA)

setA.discard("z")
print(setA)

setA.remove("z")
print(setA)