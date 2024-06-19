class Car:
    color=None
    model=None
    def car_details(self):
        print("my car details is",self.color,self.model)
car_color=input("enter car color")
car_model=input("enter car model")
car_color_ref=Car()
car_color_ref.car=car_color
car_color_ref.model=car_model
car_color_ref.car_details()