class Student:
    def __init__(self,name,percentage):
        self.name = name
        self.percentage = percentage

    def show(self):
        print("Name is", self.name,"and percentage is", self.percentage)

stud = Student("Jessa", 80)
stud.show()