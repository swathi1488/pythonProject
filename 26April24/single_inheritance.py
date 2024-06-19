class Animal:
    def car(self):
        print("lambordini")
    def speak(self):
       pass

class Dog(Animal):
    def speak(self):
        print("bow bow")
    def i_want_car(self):
        Animal().car()
d=Dog()
d.speak()
d.i_want_car()