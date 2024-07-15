# Draw a sequence of 36 straight lines to make a "starburst" design
import turtle
start_x = -200 # Starting x coordinate
start_y = 0 # Starting y coordinate
num_lines = 36 # Number of lines to draw
line_length = 400 # Length of lines
angle = 170 # Angle to turn

turtle.hideturtle()
turtle.penup()
turtle.goto(start_x,start_y)
turtle.pendown()

for x in range(num_lines):
    turtle.forward(line_length)
    turtle.left(angle)
turtle.done()