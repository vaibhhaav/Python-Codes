class P:
    def __init__(self):
        print('Parent Constructor')
    def m1(self):
        print('Parent instance method')
    @classmethod
    def m2(cls):
        print('Parent class method')
    @staticmethod
    def m3():
        print('Parent static method')
class C(P):
    @classmethod
    def m1(cls):
        super().m2()
        super().m3()

C.m1()