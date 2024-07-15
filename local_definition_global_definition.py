# Local definition (locally) overrides the global definition
x =1 # x is global
def func():
    x=2 # this x is local
    print(x) # will print 2

func()
print(x) # will print 1