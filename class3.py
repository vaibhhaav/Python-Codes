class Student:
    def __init__(self,roll_no,name,age):
        #Instance variable
        self.roll_no = roll_no
        self.name = name
        self.age = age

    # Instance method to add instance variable
    def add_marks(self,marks):
        # add new attribute to current object
        self.marks = marks

# Create object
stud = Student(100,"riya",19)
# Call Instance method
stud.add_marks(75)

# Display object
print('Roll Number: ', stud.roll_no, 'Name: ', stud.name, 'Age: ',stud.age, 'Marks: ', stud.marks)