
list1=[50,60,70,30]
list1.sort()
print("Largest Elements : ", list1[-1])


l=[30,40,50,60,60,70,8]
temp=l[0]
for i in range(1,len(l)):
    if(temp<l[i]):
       temp=l[i]
print(temp)

