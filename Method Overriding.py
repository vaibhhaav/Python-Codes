class Parent:
    def func1(self):
        print("This is parent function")

class Child(Parent):
    def func1(self):
        print("This is child function")

ob = Child()
ob.func1()
ob1 = Parent()
ob1.func1()