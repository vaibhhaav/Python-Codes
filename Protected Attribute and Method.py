class A:
    def __init__(self):
        self._my = "I am a protected attribute"
    
    def _mym(self):
        print("I am a protected attribute")

class B(A):
    def __init__(self):
        super().__init__()

    def apm(self):
        print(self._my)
        self._mym()

class C(B):
    def __init__(self):
        super().__init__()

    def ap(self):
        print(self._my)
        self._mym()

obj = C()
obj.ap()