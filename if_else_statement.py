# Compute radius of circle
import math

def main():
    radius = float(input("Enter the radius of circle: "))
    if (radius >= 0):
        area = math.pi * radius ** 2
        print('A circle with a radius of ', radius,'has an area of ', area)
    else:
        print('Negative number entered: ', radius)

main()