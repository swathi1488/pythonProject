class School:
    def student(self,name):
         self.name=name
         print("student name is",self.name)
class Varuns(School):
    def student1(self,age):
        self.age=age
        print("age is",self.age)
vs=Varuns()
vs.student("kommina")
vs.student1(30)


