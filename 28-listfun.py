# sum of two numbers using lambda function

def add (x,y):
    z=x+y
    return z
print(add(2,3))

addA = lambda x,y :x+y
q1= addA (4,5)
print(q1)

# square

square = lambda x:x*x
print(square(5))

# --------------------------------------------
# function as a paramerter to other function

mul =lambda x,y:x*y 
ans = mul(2,3)
print(f'multiplication={ans}')

add = lambda x,y:x+y 
ans1 = add(2,3)
print(f'addition={ans1}')

div = lambda x,y:x/y 
ans2 = div(10,2)
print(f'division={ans2}')

mod =lambda x,y:x%y
ans4 = mod (2,3)
print(f'modulus={ans4}')

print("-----------------------------")

# calculator
add = lambda x,y:x+y 
sub = lambda x,y:x-y 
div = lambda x,y:x/y
mul = lambda x,y:x*y
div = lambda x,y:x/y 
mod = lambda x,y:x%y 

def calculator(fn,a,b):
    res=fn(a,b)
    return res
j= 22
k= 2
cal1 = calculator(add,j,k)
print(cal1)

cal2 =calculator(sub,j,k)
print(cal2)

cal3=calculator(mul,j,k)
print(cal3)

cal4 = calculator(div,j,j)
print(cal4)

cal5=calculator(mod,j,k)
print(cal5)

#----------------------------------------------------------------

# function as return type

def add():
    return lambda x,y:x+y
def sub():
    return lambda x,y:x-y
def mul():
    return lambda x,y:x*y
def div():
    return lambda x,y:x/y
def mod():
    return lambda x,y:x%y 

# Add--------------------------

fn_add = add()
print(fn_add)
print(fn_add(11,22))

# sub

fn_sub = sub()
res = fn_sub(10,5)
print(res)

fn_mul =mul()
res = fn_mul(2,4)
print(res)

fn_div = div()
res = fn_div(30,5)
print(res)

print("-------------------------")

def addition (x,y):
    print(x+y)

addition(10,20)

# addition()     # error

# default parameter

def additionA (x=10,y=20):
    print(x+y)
additionA(100,500)
additionA()

# position arguments

def substraction(x,y):
    print(x-y)
# x=100 ,y = 50
substraction(50,100)
substraction(y=50,x=100)
