def Computegcd(x,y):

    if x > y:
        small = y
    else:
        small = x

    for i in range(1, small+1):
        if((x%i == 0) and (y%i == 0)):
            gcd = i

    return gcd


x=60
y=48

print("gcd of 60 and 48 is : ", end="")
print(Computegcd(60,48))


        