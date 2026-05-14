# =======================================================================
# Generators ans Decorators in python
# =======================================================================

# Part 1 : Generators

# Important Note:
# return ===ends the function completely
# yield ==== pauses the function and returns value one by one
# ----------------------------------------------------------

# Example 1 : return statement

# -------------------------------------------------------

def gen_numbers():
    return 1 
    return 2
    return 3
    return 4
res1 = gen_numbers()
print(res1)

res1 = gen_numbers()
print(res1)

# -----------------------------------------------------
# Example 2: return multiple values using list
# ---------------------------------------------------------

def gen_numbers2():
    return[1,2,3,4]

res1 = gen_numbers2()
print(res1)

print("------------------------------")

# -------------------------------------------------
# Example 3: Genertor using yield
# --------------------------------------------------

# A generator is a special type of function 
# that returns values one by one using yield

def gen_numbers3():
    yield 1
    yield 2
    yield 3
    yield 4

gen = gen_numbers3()
print(gen)                   # < generator object gen numbers at 0x000002B1C4E153C0>

# Next
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# print (next(gen))             # error: stop Iteration

print("------------------------------------------")

# -----------------------------------------------------------
# Example 4 : Infinite generator
# ----------------------------------------------------------

def infinite_numbers4():
    n = 1
    while True:
        yield n
        n = n+1

gen2 = infinite_numbers4()

print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))


print("---------------------------------------")

# -------------------------------------------------------
# Example 5 : Generator with for loop
# --------------------------------------------------

def gen_numbers4():
    yield 10
    yield 20
    yield 30
    yield 40
    yield 50

for x in gen_numbers4():
    print(x)

print("----------------------------------------")

# --------------------------------------------------
# Examplle 6 : Generator for squares
# ------------------------------------------------

def square_generator():
    for i in range (1,6):
        yield i*i 

for values in square_generator():
    print(values)

print('-----------------------------------------------------')


# ------------------------------------------------------------------------

def square_generator2(start,stop):
    for i in range (start,stop+1):
        yield i*i 

for values in square_generator2(5,10):
    print(values)

print("----------------------------------------------")

# =============================================================================================

# Decorators in python - explanation

# ============================================================================================

# Decorator means:

# Before a functions runs - do something
# Run the original function
# After functions runs - do something

# Real - life Example:
# Before entering office - security check
# Enter office - main work
# After work - exit process

# syntax

# def decorator_name (func):
#   def wrapper():
#     before stmts
#     funct
#     after stmts
# return wrapper
# func - original function
# wrapper - extra functionality holder

# -------------------------------------------------------------
# Example 1 : basic Decorator
# -----------------------------------------------------------

# step 1 : Defining Decorator

def my_decorator(func):
    def wrapper():
        print("I am before function call")
        func
        print("I am after function call")
    return wrapper
# step 2: Using decorator

@my_decorator
def say_hello():
    print("I am original function")

# step3 : calling function
say_hello()

# Explanation

# say_helo()= my_decorator (say hello)
# print("I am before func call")
# say_hello function call (print("I am origial function"))
# print("I am after function call")

# -----------------------------------------------------------------
# Example 2 : Decorator with parameters
# -----------------------------------------------------------------

def my_deco(myfunc):
    def wrapper(a,b):
        print(f"Adding {a}and {b}")
        result = myfunc(a,b)
        print(f"Result={"result"}")
    return wrapper
@my_deco
def add(x,y):
    return x+y 

# call
add (100,200)

# Explanation

# add (100,200)=my_deco(add)
# print(f"adding {a}and{b}")
# myfunc (a,b)(add(a,b))
# print(f"Result = {result}")

 