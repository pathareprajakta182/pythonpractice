# herarachical Inheritance

class Mother:
    def __init__ (self,mfn,ln):
        self.mfname = mfn 
        self.lname = ln 

    def displayMName(self):print(f"mother name={self.mfname} surname = {self.lname}")

class Daughter(Mother):
    def __init__ (self,mfn,ln,dfn):
        super(). __init__ (mfn,ln)
        self.dfname = dfn 
    
    def displayDName (self):
        print(f'daughter name={self.dfname} surname ={self.lname}')

class Son(Mother):
    def __init__ (self,mfn,ln,sfn):
        super(). __init__(mfn,ln)
        self.sfname =sfn 
    
    def displaySName(self):
        print(f'son name={self.sfname} surname={self.lname}')

s = Son("dipti","masalkar","aditya")
s.displayMName()
s.displaySName()
print(s.lname)
print(s.sfname)
print(s.mfname)

print("---------------------")

d = Daughter("rucha","gaware","rajasi")
d.displayMName()
d.displayDName()
print(d.lname)
print(d.mfname)
print(d.dfname)

print("----------------------")

m = Mother("prajakta","pathare")
m.displayMName()
print(m.lname)
print(m.mfname)

print("------------------------")

# ---------------------------------------------------------------------------------------

# multi level inheritance

class Mother:
    def __init__ (self,mfn,ln):
        self.mfname = mfn
        self.lname = ln 

    def displayMName(self):
        print(f'mother name ={self.mfname} surname ={self.lname}')

    def greet(self):
        print(f"This is Hello from {self.mfname}...")

class Father:
    def __init__(self,ffn,ln):
        self.ffname = ffn 
        self.lname = ln 
    
    def diaplayFName(self):
        print(f'father name ={self.ffname} surname ={self.lname}')

    def greet(self):
        print(f"This is Hello from {self.ffname}...")


class Daughter(Father,Mother):
    def __init__ (self,mfn,ln,ffn,dfn):
        Father.__init__ (self,ffn,ln) 
        Mother. __init__ (self,mfn,ln) 
        self.dfname = dfn 

    def displayDName(self):
        print(f'daughter name ={self.dfname} surname = {self.lname}') 


dt = Daughter("dipti","masalkar","niranjan","dipanshu")

dt.diaplayFName()
dt.displayMName()
dt.displayDName()

print(dt.ffname)
print(dt.lname)
dt.greet()      # by default father method is called coz father is left side


# solution is change side or function name of mother

# wht mother is not called?
# beacause Python follows  MRO (Method Resolution Order) and checks parent classes from left to right.

# since father is written first
print("--------------------------")
m = Mother("prajakta","pathare")
m.displayMName()
print(m.lname)
m.greet()

print("------------------")

f = Father("narayan","pathare")
f.diaplayFName()
print(f.lname)
f.greet()
