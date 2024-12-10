list1=[1,3,5,7,6,3,8,3,5,2,3,5,2,3]
list1.sort()
# mode =3
dict1={}
for i in list1: #i=0-x
    list1.count(i)    # count kiya kitne present hai
    dict1[i]=list1.count(i)
    list1.remove(i)
print(dict1)
x=max(dict1.values())
for key,value in dict1.items():
    if value==max(dict1.values()):
        print(key)  #3,5,2
