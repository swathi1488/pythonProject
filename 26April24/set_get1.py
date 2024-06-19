class Password:
    def __init__(self,password):
        self.__password=password
    def get_password(self,is_auth):
        if is_auth:
         return self.__password
        else:
            print("error")
    def set_password(self,password):
        if len(password)>10:
            self.__password=password
        else:
            print("week password")
    def print_len(self):
        print("length of a password",len(self.__password))
pwd=Password("hacker123")
pwd.print_len()
output=pwd.get_password(True)
print(output)
pwd.set_password("pramod@1233")
pwd.print_len()
