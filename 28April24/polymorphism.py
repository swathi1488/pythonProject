class Shape:
    def area(self):
        print("this is shape")
class Rectangle:
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath
    def area(self):
        return self.length*self.breath
class Circle:
    def __init__(self,radius):
         self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
r=Rectangle(5,10)
print(r.area())
c=Circle(10)
print(c.area())
s=Shape()
s.area()