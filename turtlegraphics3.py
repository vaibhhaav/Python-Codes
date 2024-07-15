# Interesting circle loops design by repeatedly drawing a simple shape, with the turtle tilted at a slightly different angle each time it draws the shape
import turtle
num_circles = 36
radius = 100
Angle = 10

for x in range(num_circles):
    turtle.circle(radius)
    turtle.left(Angle)
turtle.done()