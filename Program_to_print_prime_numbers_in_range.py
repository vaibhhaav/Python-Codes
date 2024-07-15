lower = eval(input("Enter a lower range: "))
upper = eval(input("Enter an upper range: "))
for n in range(lower, upper+1):
    if n>1:
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            print(n)