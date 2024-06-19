#hiding the implementation and show important details

from abc import ABC , abstractmethod
class Animal:
    @abstractmethod
    def sound(self):
        print("doog sound")
class Dog(Animal):
    def sound(self):
        return "Bow Bow"
class Cat(Animal):
    def sound(self):
        return "meow meow"
class Tiger(Animal):

    def sound(self):
       return "grar gear giiii!!!"
# who ever extends from the parent we have to complete it
d=Dog()
print(d.sound())
c=Cat()
print(c.sound())
t=Tiger()
print(t.sound())
