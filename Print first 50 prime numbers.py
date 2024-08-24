def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

count = 0
i = 2
primes = []

while count<50:
    if is_prime(i):
        primes.append(i)
        count += 1
    i += 1

for j in range(0,50,10):
    print(" ".join(str(p) for p in primes[j:j+10]))