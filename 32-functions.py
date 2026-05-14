# map, filter ,reduce, list comprehensions

# program 1

nos = [1,2,3,4,5,6,7,8,9]

# operation with every element

sq = [x*x for x in nos]
print(sq)

sq2= list(map(lambda x: x*x,nos))
print(sq2)

# program 2

names= ['virat koholi' , 'sachin tendulkar', 'rohit shrama','ms dhoni']

print(f'names are:{list (map(lambda x :x.split(' ')[0],names))}')

namex = 'virat koholi sachin tendulkar'
q1 = namex.split(" ")
print(q1)
print(q1[0])
print(q1[1])

namex = 'virat111@gmail.com'
print(f"surname are = {list(map(lambda x :x.split(' ')[1],names))}")

nm = [x.split(' ')[0]for x in names]
print(f"name ={nm}")
snm=[x.split(' ')[1]for x in names]
print(f"surname={snm}")

# --------------------------------------------------------------------------

# program 3

numbers = [11,45,67,78,90,54,34,12,67,88,99,68,35,36]

even = [x for x in numbers if x%2==0]
print(even)

odd = [x for x in numbers if x%2!=0]
print(odd)

print(f"even numbers are = {list(filter(lambda x :x%2==0,numbers))}")

print(f"odd numbers are = {list(filter(lambda x :x%2!=0,numbers))}")

# ---------------------------------------------------------------------------------

# program 4


from functools import reduce
nos = [1,2,3,4,5,6,7,8,9,10]

print(f"addition={reduce(lambda total , x:total+x,nos,0)}")

print(f"multiplication={reduce(lambda mult , x:mult*x,nos,1)}")

