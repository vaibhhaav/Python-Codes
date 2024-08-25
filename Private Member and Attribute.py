class B:
    def __init__(self,a,b):
        self.__a = a
        self.__b = b
    
    def __d(self):
        print("B", self.__b)

b = B(1234567890, 5000)
b.__d()