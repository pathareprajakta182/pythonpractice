# incorrect way

class Student:
    def __init__ (self,fn,ln):
        self.fname = fn
        self.lname = ln

    def displayName(self):
        print(f"name={self.fname} surname={self.fname}")

class Teacher:
    salary = 20000
    def __init__ (self,fn,ln):
        self.fname = fn
        self.lname = ln 

    def displayName(self):
        print(f"name={self.fname} surname={self.fname}")

    def displaySalary(self):
        print(self.salary)
        

# inheritance

# single inheritance

# parent class

class Student:
    def __init__ (self,fn,ln):
        self.fname = fn 
        self.lname = ln 
    def displayName(self):
        print(f'name={self.fname} surname={self.lname}')

# child class

class Teacher (Student):
    salary = 20000
    def displaySalary(self):
        print(self.salary)

dip = Teacher("dipanshu","chawde")
dip.displayName()
dip.displaySalary()
print(dip.lname)
print(dip.fname)
print(dip.salary)

      
stu = Student("neel","chawde")
stu.displayName()
print(stu.fname)
print(stu.lname)
