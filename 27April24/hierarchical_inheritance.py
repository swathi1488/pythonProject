class BigVehicle:
    def bigvehicle_method(self):
        return "this is Bigvehicle"
class Vehicle(BigVehicle):
    def info(self):
        return "this is vehicle"
class Car(Vehicle):
    def info(self):
        return "this is car"
class Bycycle(Vehicle):
    def info(self):
        return "this is a bycycle"
c=Car()
b=Bycycle()
print(c.bigvehicle_method())
print(b.bigvehicle_method())
print(c.info())
print(b.info())