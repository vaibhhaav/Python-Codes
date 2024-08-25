class A():
    def method1(self):
        print("This is method 1")

class B(A):
    def method2(self):
        print("This is method 2")
    
class C(A):
    def method3(self):
        print("This is method 3")

class D(B,C):
    def method4(self):
        print("This is method 4")

ob = D()
ob.method1()
ob.method2()
ob.method3()
ob.method4()