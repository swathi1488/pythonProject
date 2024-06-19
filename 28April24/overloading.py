# overloading python not supported in the traditional sense

class MathUtil:
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        return a+b+c
m=MathUtil()
m.add(1,2)
op=m.add(1,2,3)
print(op)