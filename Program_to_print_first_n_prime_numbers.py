number = int(input("Enter number of prime numbers to be displayed: "))
count = 1
n = 2
while(count<=number):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        print(n)
        count=count+1
    n=n+1
