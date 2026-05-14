a=[1,2,3,4]
print(a)
print(type(a))

a= "dipanshu"
print(a)
print(type(a))

a = 11
print(a)
print(type(a))

a = {"name":"dipanshu"}
print(a)
print(type(a))


# class --->
# methods , properties

# type
# introvert               extrovert
# calm                     loud
# less outing             more outing
# less social             more social

# Human
# properties --> name , hight , weight .....
# method ---> walk(),talk()

# method -----> healthy , discuss, solution , motivate


# vehicle
# properties ----> colour , model logo , company  
# methods ----> start(), stop(), move()


# bank 
# properties ----> account , account name , branch name , balance
# methods ----> deposit(), withdraw()

# program 1

# class , object , properties , methods


class Person:
    # properties
    fname = None
    lname = None 
    # method
    def displayName(self):    # self =====> object
        print(f"Name={self.fname} and surname = {self.lname}")

# self ====> adi
adi = Person()
print(adi.fname)
print(adi.lname)

adi.fname="aditya"
adi.lname = "masalakar"
adi.displayName()

print(adi.fname)
print(adi.lname)

# self ====> dip

dip = Person()
print(dip.fname)
print(dip.lname)

dip.fname = "dipanshu"
dip.lname = "chawde"
dip.displayName()
print(dip.fname)
print(dip.lname)

# a = [1,2,3,4,5,6]
# a.pop()

print("--------------------------------")

# program 2

# constructor
# a constructor is a speacial method in a class that is automatically called a new object is created.
# its main purpose is to initialize the object's attributes (set intital values) when the object is instantiated.
# __init__

class Person2:
    # constructor
 def __init__(self,fn,ln):
        self.fname = fn 
        self.lname = ln

# method
 def displayName(self):    # self ====> object
    print(f"name ={self.fname} and surname ={self.lname}")  

adi2 = Person2 ("aditya2" ,"masalkar2")  
adi2.displayName()
print(adi2.fname)
print(adi2.lname)

dip2 = Person2("dipashu2","chawde2")
dip2.displayName()
print(dip2.fname)
print(dip2.lname)

# key Points of constructor:
# The first parameter is always self , which refers to the current object.
# You can have default values for parameters.


#  program 3


class Person3:
    def __init__(self):
        self.fname = None
        self.lname = None
    # method
    def displayName(self):            # self =====> object
        print(f"name = {self.fname} and surname={self.lname}") 

adi3 = Person3()
print(adi3.fname)
print(adi3.lname)

adi3.fname ="aditya3"
adi3.lname = "masalakar3"
adi3.displayName()
print(adi3.lname)
print(adi3.fname)

print("--------------------------------")

# program 4
# class level variable

class Bank:
    # class level variable
    country = "India"

    def __init__(self,fn,accNo,bal):
        self.fname = fn 
        self.accountNo = accNo 
        self.balance = bal
    def deposit(self,amount):
        self.balance = self.balance+amount
        return self.balance
    
    def withdrawl(self,amount):
        if amount < self.balance:
         self.balance=self.balance-amount
         return self.balance
        else:
          return "Insufficient balance"
        
dip = Bank("dipanshu",1234,10000)
print(dip.fname)
print(dip.balance)
print(dip.accountNo)
print(dip.country)

newBal = dip.withdrawl(15000)
print(newBal)

    
newBal = dip.deposit(10000)
print(newBal)

print("--------------------")

adi = Bank("aditya",6666,50000)
print(adi.fname)
print(adi.balance)
print(adi.accountNo)
print(adi.country)

newBal = adi.withdrawl(10000)
print(newBal)

newBal= adi.deposit(25000)
print(newBal)