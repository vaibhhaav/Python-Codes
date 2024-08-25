class Shape:
    def draw(self):
        print("Drawing shape")

class Circle(Shape):
    def draw_circle(self):
        print("Drawing circle")

class ColoredCircle(Circle):
    def draw_colored_circle(self):
        print("Drawing colored circle")

my_circle = ColoredCircle()
my_circle.draw()
my_circle.draw_circle()
my_circle.draw_colored_circle()