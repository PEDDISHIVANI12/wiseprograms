n1 = int(input("enter the starting number"))
n2 = int(input("enter the ending number"))
list1 = []
def primes(n1,n2):
    for i in range(n1,n2):
        for j in range(2,i+1):
            if(i %j == 0):
                list1.append(i)
    return list1
print(sum(primes(n1,n2)))




