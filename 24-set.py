a = 20
print(a)
print(type(a))

a=20.5
print(a)
print(type(a))

a= "dipanshu"
print(a)
print(type(a))

a= True
print(a)
print(type(a))

a= [11,22,33]
print(a)
print(type(a))

a= { "fn":"neel"}
print(a)
print(type(a))

a= (20,50)
print(a)
print(type(a))


# set-------------
# does not store duplicate value
# unordered list

a = {11,22,33}
print(a)
print(type(a))

a = { 20,30,10,30,10,20}
print(a)
print(type(a))

# can we acces set elements by index      # No
# set1={"a","b","c","d"}
#print(set1[0])                          # TypeError:"set"object is not subscriptable

a={11,22,33,44,55}
print(44 in a)
print(77 in a)


# loops---------
# for , for with range, while

# find the length , min , max of set

set2 = {77,3,90,78,65,24,11,4,99}
print(len(set2))

print(max(set2))
print(min(set2))

# for-----------

for x in set2:
    print(x)

print("----------------------")
#for with range function
#for x in range (len(set2)):       # start index=0 end index=9 stepsize=1
    #  print(x)

# list
list1 = [10,20,30,40,52]
for x in range(len(list1)):       # 
   # print(x)
     print(list1[x])

for x in list1:
     print(x)

print("---------------")

set2 = { 77,3,90,75,65,24,11,4,99}
for x in set2:
     print(x)

# we can not use range function
# for x in range(len(set2)):
#   print(x)
#   print(set2[x])   # TypeError:'set'object is not subscriptable

# whilee
# i = 0
#while(i<len(set2)):
#  print(set2[i])   # TypeError: 'set'object is not subscriptable 
#  i= i+1

# set methods
# add element
set3 = {1,2,3,4,5}
print(set3)
set3.add(66)
print(set3)

# clear set-----------------
set3 = {1,2,3,4,5}
set3.clear()
print(set3)

# pop---------
set3 = {1,2,3,4,5}
set3.pop()
print(set3)

# remove---------

set3 = {31,42,53,84,75}
set3.remove(75)
print(set3)

# sets in python are unordered collections.
# That means the elements inside a set do not maintain any specific order
# - not by insertion order , not sorted order.


# update---------

setA = {33,44,55,66}
setA.update([77,22,11])
print(setA)

setB = { 11,22,33,44}
setB.update(('a','b','c','c'))
print(setB)

setC = {11,22,33,44}
setC.update({'a','b','c','c'})
print(setC)

setC = {11,22,33,44}
setC.update("neel")
print(setC)
print("-------------------------")
      
setD={11,12,13,14,15,16}
setE = setD
setD.update({'a','b'})
print(setD)
print(setE)

print("--------------------")

setD = {11,12,13,14,15,16}
setE = setD.copy()
setD.update({'a','b'})
print(setD)
print(setE)





































