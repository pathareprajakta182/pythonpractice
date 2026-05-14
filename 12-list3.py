#listA=[33,44,11,-9,800,754,6354,12,38]
#new_listA=sorted(listA)
#print(listA)
#print(new_listA)

listB=["dip","nil","praju","dipashu","adi","zshan"]
new_listB=sorted(listB)
print(listB)
print(new_listB)

new_listB=sorted(listB,reverse=True)
print(listB)
print(new_listB)


# count()-----------------------------

listB= ["dip","nil","praju","dipashu","dip","nil","zshan","praju","nil","adi","zshan"]
print(listB.count("praju"))

print(listB.count("nil"))
print(listB)

# sort----------------------
print('-------------------------')
words = ["apple","banana","kiwi","mango","orange","papaya","grapes","fig"]

#print(words)
#words.sort()
#print(words)

words.sort(key=str.lower)
print(words)

       
    


