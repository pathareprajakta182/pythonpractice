x=10
y=20

#functions with parameter and without return type

def calc(a,b):         # a,b, parameter
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a%b)
calc(x,y)             # x,y ,arguments

print("-------------------")

# functions with parameter and with return type

def add(a,b):
    return a+b
res = add (x,y)
print(res)

res2 = add(15.5,63.1)
print(res2)

res3 = add("dip","anshu")
print(res3)

#print("_----------------")

# find were person can drive or not
# age
# int as parameter and boolean as return type

def canDrive(age):
    if age >=18:
        return "canDrive"
    else:
        return "can not Drive"
    
    res=canDrive(10)
    print(res)

    res = canDrive(32)
    print(res)

    print("-----------")
    # string as parameter and string (with concatination)as return type

    def greet(name):
        return "hello "+name +".....How are you?" 
    print(greet("dipanshu")) 

    # list as parameter and list as return type

    city = ["pune","nashik","mumbai","nagpur","nanded"]

    def addcity(cityList,cityName):
        cityList.append(cityName)
        return cityList
    
    print(city)
    city2 = addcity(city,"amravati")
    print(city2)