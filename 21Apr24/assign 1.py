class Car:
    seat=None
    enginee=None
    color=None
    model=None
    fuel=None

    def car_break(self):
        print("beak working properly")
    def streaing(self):
        print("streaing")
    def driving(self):
        print("driving")
    def speed(self):
        print("speed")
    def exlator(self):
        print("exlator")
car_details_obj_ref=Car()  #car() object created,car_details_obj(reference)
car_details_obj_ref.seat="pushable"
car_details_obj_ref.enginee="v3"
car_details_obj_ref.color="black"
car_details_obj_ref.model="v001"
car_details_obj_ref.fuel="petrol"

print(car_details_obj_ref)

car_details_obj_ref.car_break()
car_details_obj_ref.driving()
car_details_obj_ref.exlator()
car_details_obj_ref.streaing()
car_details_obj_ref.speed()


