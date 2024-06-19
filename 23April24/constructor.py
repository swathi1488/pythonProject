class Person:

    def __init__(self,name):
      self.name=name
      print("you are created object")
    def print_details(self):
        print("your details are",self.name)

amith=Person("amith")
amith.print_details()
pramod=Person("pramod")
pramod.print_details()
