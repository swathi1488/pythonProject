class Parent:
    def fun1(self):
        print("this is fun 1")
class Child(Parent):
    def fun2(self):
      print("this is fun2")
c=Child()
c.fun1()
c.fun2()
