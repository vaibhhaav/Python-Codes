class Parent():
    def func1(self):
        print("This is function 1")

class Child(Parent):
    def func2(self):
        print("This is function 2")
    
class Child1(Parent):
    def func3(self):
        print("This is funciton 3")

class Child2(Child,Child1):
    def func4(self):
        print("This is function 4")

ob = Child2()
ob.func1()
ob.func2()
ob.func3()
ob.func4()