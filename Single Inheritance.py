class Parent:
    def func1(self):
        print("This is function one")

class Child(Parent):
    def func2(self):
        print("This is function two")

ob = Child()
ob.func1()
ob.func2()