# it supported when we call default method


class MathUtil:
     def add(self,a,b=0,c=0):
         return a+b+c
m=MathUtil()
print(m.add(1,2))
print(m.add(1,2,3))
print(m.add(1))
