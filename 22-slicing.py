# string[startindex : endindex (not included): step size(1)]
       #1   2  3  4  5  6  7  8  9  10
city = "c   h  a  n  d  r  a  p  u  r"
      #-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 
print(city[1::])                # handrapur
print(city[2:6:])               # andr
print(city[-8:7:])              # andra
print(city[-8:-1:])             # andrapu
print(city[1:-1:])              # handrapu
print(city[-1:-4:])             # empty string
print(city[-1:4:])              # empty string
print(city[-10:4:])             # chan
print(city[::2])                # cadau
print(city[::-1])               # reverse string (rupardnahc)
print(city[-1:-8:-1])           # rupardn
print(city[-4:-1:-1])           # empty string