# Class Variable vs instance variable

class students:
    # class variable
    country="India"

    # instance variable using constructor
    def __init__(self,fn,ln,age):
        # instance variable
        self.fname = fn
        self.lname = ln 
        self.age = age 

    @classmethod 
    def changeCountry(cls,nc):
        cls.country=nc 

    # instance method
    def displayName(self):
        print(f"name={self.fname} and surname= {self.lname}")

    # instance method
    def updateAge(self,inc):
        self.age =self.age+inc 

tan = students("tanish","chawde",18)
print(tan.fname)
print(tan.lname)
print(tan.age)
print(tan.country)

tan.displayName()

tan.updateAge(2)
print(tan.age)

# tan.changeCountry("UK")    # this changes value of class variable
tan.country ="UK"             # this changes value of object variable
print(tan.country)

print("_--------------------------------")

raj= students("rajsi","gaware",10)
print(raj.age)
print(raj.lname)
print(raj.fname)
print(raj.country)

print("---------------------")
print(raj.lname)
print(raj.fname)
raj.country = "germany"
print(raj.country)

raj.displayName()

raj.updateAge(5)
print(raj.age)

#raj.changeCountry("USA")    # this changes value of class variable
raj.country = "USA"
print(raj.country)

print(tan.country)

ak = students("Akay","masalkar",30)
print(ak.fname)
print(ak.country)
print(ak.age)
ak.updateAge(2)
print(ak.age)
print("---------------------")

students.changeCountry("Bharat")
print("-----------------------------****")
print(tan.country)
print(raj.country)
print(ak.country)
    