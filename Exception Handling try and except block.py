class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name,age)
        self.salary = salary

    def display(self):
        super().display()
        print(f"Salary: ${self.salary}")

    def set_salary(self, salary):
        try:
            if salary < 0:
                raise ValueError("Salary cannot be negative")
            self.salary = salary
        except ValueError as e:
            print(f"Error: {e}")

person = Person("Alice", 30)
employee = Employee("Bob", 40, 50000)

person.display()
employee.display()

employee.set_salary(-10000)

employee.set_salary(60000)
employee.display()