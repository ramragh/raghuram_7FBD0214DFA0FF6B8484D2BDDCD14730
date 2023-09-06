def factorial(n):
    fact=1
    if int(n) >= 1:
        for i in range (1,int(n)+1):
            fact = fact * i
        return fact

num = int(input("Enter the number: "))

print("factorial of ",num,": ",end="")
print(factorial(num))
