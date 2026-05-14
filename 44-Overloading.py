# overloading - same class, same method but different parameters

# public class 

class Calculator:
    def addition(self, a=None , b=None, c= None , d= None):
        if a != None and b != None and c !=None and d !=None:
             print(a+b+c+d)

        elif a !=None and b !=None and c !=None:
            print(a+b+c)

        elif a !=None and b !=None:
            print(a+b)
        
        else:
            print("atlist 2 values are required")

cc = Calculator()
cc.addition(1,2)
cc.addition(5,6,4)
cc.addition(1,5,4,7)
cc.addition(1)
