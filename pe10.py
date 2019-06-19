def is_prime(n):
    for i in range(2,round(num**0.5)+1):
        if num % i == 0:
            return False
    return True
    prime_sum = 0
    for i in range(2,2000000):
        if is_prime(i):
            prime_sum += 1
    print(prime_sum)
