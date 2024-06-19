class Animal:
    def sound(self):
        print("this is animal")
class Dog(Animal):
    def sound(self):
      print("dog sound")
class Cat(Animal):
    def sound(self):
        super().sound()
        print("cat sound")
c=Cat()
c.sound()
d=Dog()
d.sound()
a=Animal()
a.sound()