class Person: 
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")

# Create instances of the class 
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Access attributes and call methods
print(person1.name)
person2.say_hello()

