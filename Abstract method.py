from abc import *
class Demo1(ABC):
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass
    def m3(self):
        print("Implemented method")

class Demo2(Demo1):
    def m1(self):
        print("m1 method implemented")
    
    def m2(self):
        print("m2 method implemented")

c = Demo2()
c.m1()
c.m2()
c.m3()