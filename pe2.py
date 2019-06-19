palindrome = lambda num:str(num) == str(num)[::-1]
product ={i*j for i in range(100,1000) for j in range(100,1000)} 
palindromes = filter(palindrome,product)
print(max(palindromes))



