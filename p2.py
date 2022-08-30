int_wall= int(input())
ext_wall= int (input())
sum=0
for i in range(0,int_wall):
        x= float(input())
        sum += 18 * x
for i in range(0,ext_wall):
        x= float(input())
        sum += 12 * x        

print(sum)        
print("Total Estimated Cost : ", sum)


