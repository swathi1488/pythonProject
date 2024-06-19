class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def get_name(self,):
        return self.__name,self.__age
    def set_name(self,name,age):
      self.__name=name
      self.__age=age

    def print_details(self):
        print("your details are...>",self.__name,self.__age)
per=Person("swathi",27)
per.print_details()
per.set_name("kommina",30)
per.get_name()
per.print_details()