class Flyable:
    def fly(self):
        print("Can fly")

class Swimmable:
    def swim(self):
        print("Can swim")

class FlyingFish(Flyable,Swimmable):
    pass


nemo = FlyingFish()
nemo.fly()
nemo.swim()