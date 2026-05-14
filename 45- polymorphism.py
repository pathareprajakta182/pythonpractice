# polymorphism

# overloading
class Mathops:
    def add(self, a=0 , b=0, c=0 , d=0):
        return a+b+c+d 
    
a= Mathops()
print(a.add(1,2))
print(a.add(1,2,3))
print(a.add(1,2,3,4))
print(a.add())

# overriding :: same method different class

class Animal:
    def sound(self):
        print("basic generic sound")

class Dog(Animal):
    def sound (self):
        print("bho bho")


class Cat(Animal):
    def sound (self):
        print("mew mew")


class Duck(Animal):
    def sound (self):
        print("quack quack")


class Rabit(Animal):
    def display(self):
        print("i am rabit...i dont make sound...")

a=Animal()
b=Dog()
c=Cat()
d=Duck()
e=Rabit()

a.sound()
b.sound()
c.sound()
d.sound()
e.sound()
e.display()

print("----------------------------")
for animal in (a,b,c,d,e):
    animal.sound()

# same class same method different signature - overloading
# differnt class same method same signature - overriding

# program 3

# Duck typing means:"If it looks like a duck and behaves like a duck , then treat it like a duck".

# In Python, it means:
#- Python does not care about the object has the required method

print("----------------------")

class Duckk:
    def speak(self):
        return "quack"
    
class Human:
    def speak(self):
        return"hi...hello"
    
class Catt:
    def speak(self):
        return "mew"
    
def call_speak(obj):
    print(obj.speak())
    
dk = Duckk()
ct = Catt()
hm = Human()

call_speak(dk)
call_speak(hm)
call_speak(ct)

    





