class Myclass():
    name=None

    def my_name(self,last_name):
        print("my name is...>",self.name,last_name)

name_obj_ref=Myclass()
name_obj_ref.name="swathi"
name_obj_ref.my_name("kommina")