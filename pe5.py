import math
n = int(input("enter the number"))
fact = math.factorial(n)
res = [int(x) for x in str(fact)]
print(sum(res))


