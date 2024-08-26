class Demo:
    def __init__(self):
        print('No-Arg Constructor')
    def __init__(self,a):
        print('One-Arg Constructor')
    def __init__(self,a,b):
        print('Two-Arg Constructor')

d1 = Demo(10,20)