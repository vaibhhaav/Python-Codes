def gcd(a,b):
    gcd_value = 1
    for i in range(1, min(a,b) + 1):
        if a % i == 0 and b % i == 0:
            gcd_value = i
    return gcd_value

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = gcd(num1,num2)
print("The Greatest Common Divisor of", num1, "and", num2, "is", result)