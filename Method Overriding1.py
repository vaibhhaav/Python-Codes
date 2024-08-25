class Rectangle:
    slides = 4
    all_sides_equal = False 
    opposite_sides_equal = True
    type = 'rectangle'

    def area(self):
        length = int(input('Enter length: '))
        width = int(input("Enter width: "))
        return length * width

class Square(Rectangle):
    all_sides_equal = True
    type = 'square'

    def area(self):
        side = int(input("Enter side: "))
        return side**2

a = Rectangle()
print(a.area())
b = Square()
print(b.area())