class Vehicle:
    def drive(self):
        print("Vehicle is being driven")

class Car(Vehicle):
    def drive_car(self):
        print("Car is being driven")

class Motorcycle(Vehicle):
    def drive_motorcycle(self):
        print("Motorcycle is being driven")

my_car = Car()
my_motorcycle = Motorcycle()

my_car.drive()
my_car.drive_car()

my_motorcycle.drive()
my_motorcycle.drive_motorcycle()