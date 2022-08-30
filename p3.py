n = int(input())
k = int(input())
j = int (input())
m = int(input())
p = int(input())

s =0
s += int(m/k)
s += int(p/j)
print("Number Of monkeys left on the tree : ",  n-s)