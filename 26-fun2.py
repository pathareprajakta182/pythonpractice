 # list as parameter and list as return type

city = ["pune","nashik","mumbai","nagpur","nanded"]

def addcity(cityList,cityName):
        cityList.append(cityName)
        return cityList
    
print(city)
city2 = addcity(city,"amravati")
print(city2)

# dict as parameter and as return type

info = {
        "name"  :"dipanshu",
        "lname" :"chawade"

}
def addcityy(info):
        info["city"]="pune"
        return info
print(info)
info2=addcityy(info)
print(info2)
print(info)

#tuple as parameter and tuple as return type

numbers = (11,22,33)
def addToTuple(tupA):
        tupA=list(tupA)
        tupA.append(55)
        tupA=tuple(tupA)
        return tupA
print(numbers)
finalTuple= addToTuple(numbers)
print(finalTuple)
print(numbers)

# set as parameter and set as tetrun type

setA = {1,2,3,4,5}
def addToset(setB):
        setB.add(66)
        return setB
        print(setA)

        setF = addToset(setA)
        print(setF)
        print(setA)

        
        
        
        