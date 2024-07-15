n=eval(input("Enter a number: "))
for i in range(1,n,1):
    if(i%5==0 and i%10!=0):
        print(i)