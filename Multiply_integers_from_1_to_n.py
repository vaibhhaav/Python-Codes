# Return the result of multiply the values from 1 to n. This is the factorial function. We assume n>=0
def multiply_to_n(n):
    result = 1
    for i in range(2,n+1):
        result *= i
    return result

print(multiply_to_n(5))