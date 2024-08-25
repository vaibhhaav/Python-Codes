class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return 'blah blah'

class Dog(Animal):
    def __init__(self, name, species, color):
        super().__init__(name, species)
        self.color = color

    def speak(self):
        return 'bow bow'

class Cat(Animal):
    def __init__(self, name, species, color):
        super().__init__(name, species)

    def speak(self):
        return 'meow meow'

snow = Dog('snow','mammal','white')
oscar = Cat('oscar','mammal', 'black')

print(snow.speak())
print(oscar.speak())