import array as arr
b = arr.array('d',[1,2,3,4,5,6])
print("the newly created array is :", end=" ")
b.append(9.9)
b.insert(0,8.9)
for d in range(0,len(b)):
    print(b[d],end= " ")