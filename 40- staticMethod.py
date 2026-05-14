# instance method
# class method 
# static method - no interaction with object , writing function inside the classs

# object instance of class

# program 1

import random 

class StringUtilities:
    @staticmethod
    def make_upper(str):
        return str.upper()
    
    # email validater @ , minskole.in
    @staticmethod
    def vali_email(str):
        return "@" and "minskole.in" in str 
    
    @staticmethod
    def valid_email(str):
        if("@" in str and "minskole.in" in str):
            return "valid email"
        else:
            return"Invalid email"
        
        #id_generator
        def generator():
            return random.randint(1000,9999)

print(StringUtilities.make_upper("dipanshu"))
print(StringUtilities.valid_email("dipanshu@minskole.in"))
print(StringUtilities.valid_email("dipanshu@minskole.com"))

# program 2

class Employee:
    # class variable
    country ="India"

    def __init__(self,name,empid,salary):
        # instance variable

        self.fullName = name 
        self.empid =empid 
        self.salary = salary

# instance method

    def displayName(self):
        print(f"name={self.fullName}")

    # class method

    @classmethod
    def changeCountry(cls,nc):
        cls.country=nc 

    # static method
    @staticmethod
    def calculateBonus(sal):
        return sal*0.10


# instance method

    def displayFinalSalary(self):
        return Employee.calculateBonus(self.salary)+ self.salary

print("------------------------")

e1 = Employee("dipanshu chawde",11,10000)
e2 = Employee("aditya masalkar",22,20000)
e3 = Employee("rucha gaware",33,30000)

print(e1.displayFinalSalary())
print(e1.displayName())
print(e1.country)
# e1.changeCountry("UK")
e1.country = "UK"
print(e1.country)

print("------------------")

print(e2.displayName())
print(e2.displayFinalSalary())
print(e2.country)

print("--------------------")

print(e3.displayName())
print(e3.displayFinalSalary())
#print(e3.country)
e3.country ="USA"
print(e3.country)

print("---------------")

print(Employee.calculateBonus(50000))