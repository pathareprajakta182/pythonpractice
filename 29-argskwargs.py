#* args , **kwargs
# default parameter

def addA (x = 10, y = 20):
    print(x+y)

addA(11,22)
addA()

# positional arguments

def average (x,y,z):
    avg = (x+y+z)/3
    print(avg)

average(11,22,33)
average(z=100,y=200,x=300)

#===============================================

# args

def addAll(*args):
    print(args)
    print(type(args))
    total=0
    for x in args:
        total = total + x
        return total  
res = addAll(1,2,3,4,5,6,7,8)
print(res)

res = addAll(11,21,31,41,51,61,71,81)
print(res)

# kwargs

info ={
    "name":"dipanshu",
    "surname":"chawde"

}
def addCity(**kwargs):

    print(kwargs)
    print(type(kwargs))
    info.update(kwargs)

print(info)
addCity(city="pune")
print(info)

#-----------------------------------------------------

def addCity2(**kwargs):
    print(kwargs)
    print(type(kwargs))
    info.update(kwargs)

print(info)
addCity2(city="pune")
print(info)
    