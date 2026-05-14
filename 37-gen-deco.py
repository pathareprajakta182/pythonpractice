# generator
# reading large file

def read_file_normal(file_path):
    with open(file_path,"r")as f:
        return f.read()
    
content = read_file_normal("student_data.txt")
print(content)

# ----------------------------------------------------------------------------
print('***------------------------------------')
# Generator for reading a large file line by line (This is a real-life use to save memory.)

def read_file(file_path):
    with open(file_path,"r") as f:
        for line in f:
            yield line 

for line in read_file("student_data.txt"):
  print(line.strip())

# --------------------------------------------------------------

print("--------------------")

# generator expression (shortcut)

square = (x*x for x in range (5))
print(next(square))      
print(next(square))      
print(next(square))      
print(next(square))      
print(next(square))      
# print(next(square))      

# ----------------------------------------------------------------------------
print('---------------------------')

# -----------------------------------
# Decorators

# # Decorators to measure execution time

import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end= time.time()
        print(f"Time taken {end-start} seconds")
    return wrapper

@timer 
def slow_function():
    time.sleep(5)

slow_function()

print("--------------------------")

# Decorator that checks login before accessing a function(Useful in web apps.)

def require_login(func):
    def wrapper(user):
        if not user.get("logged_in"):
            print("Access Denied!")
        else:
            func(user)
    return wrapper

@require_login 
def dashboard(user):
    print("Welcome to your Dashboard")

user1 = {"name":"dipanshu", "logged_in":True}
user2 ={"name":"herry","logged_in":False}

#call
dashboard(user1)
print("_--------------------------")
dashboard(user2)


print("----------------------------")

# Decorator that validates arguments

def non_zero(func):
    def wrapper(a,b):
        if b==0:
            str ="Error: divide by zero"
            return str
        return func(a,b)
    return wrapper

@non_zero
def divide(a,b):
    return a/b 

print(divide(3,0))
print(divide(9,3))

print("-------------------")

# Decorator that logs function calls

def logger(func):
    def wrapper (*args, **kwargs):
        print(f"calling {func.__name__}with {args},{kwargs}")
        return func(*args,**kwargs)
    return wrapper

@logger

def multiply(a,b):
    return a*b 

@logger
def student_info(data,details):
    return data,details

print(multiply(5,6))
print(student_info([1,2,3],{"name":"dipanshu"}))


      
     