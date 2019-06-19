import math
n = int(input("enter the number"))
a = sum(list(pow(a,a) for a in range(1,11)))
print(str(a)[-10:])
              
