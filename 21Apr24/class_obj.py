class Person:
    name = None
    age = None
    phno = None
    address = None

    def walk(self):

        print("walking---->" , self.name)


    def eat(self):
        print("eating")


    def sleep(self):
        print("sleeping")


amith_obj = Person()
amith_obj.name = "amith"
amith_obj.age = 26
amith_obj.phno = 23456778
amith_obj.address = "nagole"

durga_obj=Person()
durga_obj.name="durga"
durga_obj.age=37
durga_obj.phno=2356677888
durga_obj.address="eluru"

print(durga_obj)
print(amith_obj)

amith_obj.walk()
durga_obj.walk()