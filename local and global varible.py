x = 1 # global definition
def func(): 
    x = 2 # local definiton
    print(x)

func()

print(x)