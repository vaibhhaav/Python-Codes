class MyClass:
    def __init__(self):
        self.my = "I am a public attribute"
    
    def mym(self):
        print("I am a public method")

obj = MyClass()
print(obj.my)
obj.mym()