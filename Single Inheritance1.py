class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog Barks")

my_dog = Dog()
my_dog.speak()
my_dog.bark()