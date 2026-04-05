# additoin of two numbers

def addA(x,y):
    return x+y
res1 = addA(10,30)
print(res1)

# lambda

addB = lambda x,y:x+y
print(addB(10,30))

# lambda ===== keyword
#x,y ======parameter
# x+y ======return
# 10,30 ====== arguments


# square

square=lambda x:x*x
print(square(4))
print(square(10))
sq = square(5)
print(sq)

# cube

cube=lambda y:y*y*y
print(cube(2))

# functions of parameter

def addition():
    fn = lambda x,y:x+y
    x=55
    y=66
    a1=fn(x,y)
    return a1

res2=addition()
print(res2)
print("---------------")

print("-------------------")

addC =lambda x,y:x+y
def addition2(fn,a,b):
    a2 =fn(a,b)
    return a2
print(addition2(addC,111,122))

print("-------------")

subA =lambda x,y:x-y
def sub(fn,x,y):
    s1=fn(x,y)
    return s1
res3 =sub(subA,100,50)
print(res3)

print(addition2(subA,200,2))
    






