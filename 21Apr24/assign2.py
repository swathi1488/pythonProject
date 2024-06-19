class Person:
    name=None
    age=None
    address=None
    def introduction(self):
        print("i am ",self.name,self.age,self.address)
    def dancing(self):
        print("i am dancing")
    def learn(self):
        print("i am learning")
name_details=input("enter a name")
age_details=input("enter age")
address_details=input("enter address")
person_obj_ref=Person()
person_obj_ref.name=name_details
person_obj_ref.age=age_details
person_obj_ref.address=address_details

person_obj_ref.introduction()


