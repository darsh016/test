'''
import array as arr
a = arr.array('d',[2.5,3.2,3.3])
print("Newly created array is :", end=" ")
for d in range(0,3):
    print(a[d], end=" ")

'''

#2d array
stu_dt=([72,85,87,90,69],[80,87,65,89,85],[9691,70,78,87])
for x in stu_dt:
    for i in x:
        print(i,end="")
print()
