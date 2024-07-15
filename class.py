class Person:
    def __init__(self,name,sex,profession):
        # data memebers (instance variable)
        self.name = name
        self.sex = sex
        self.profession = profession

# Behavior (instance methods)
    def show(self):
        print('Name:', self.name, 'Sex:', self.sex, 'Profession:', self.profession)

    def work(self):
        print(self.name, 'working as a', self.profession)

# Create object of a class
jessa = Person('Jessa','Female','Software Engineer')

# call methods
jessa.show()
jessa.work()