class Vehicle:
    def move(self):
        print("This vehicle moves in some way.")

class Car(Vehicle):
    def move(self):
        print("This car drives on roads.")

class Plane(Vehicle):
    def move(self):
        print("This plane flies in the sky.")

class Bicycle(Vehicle):
    def move(self):
        print("This bicycle pedals on roads.")

def travel(vehicle):
    vehicle.move()

my_car = Car()
my_plane = Plane()
my_bicycle = Bicycle()

travel(my_car)      
travel(my_plane) 
travel(my_bicycle)