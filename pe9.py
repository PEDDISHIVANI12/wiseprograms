n = int(input("enter the number"))
l1 = sum([i*i for i in range(1,n+1)])
s = sum([i for i in range(1,n+1)])
l2 = s**2
print(l2-l1)
