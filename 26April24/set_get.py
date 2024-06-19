class Password:
    def __init__(self,password):
        self.__password=password
    def get_password(self):
        return self.__password
    def set_password(self,password):
        if len(password)>10:
            self.__password=password
        else:
            print("week password")

    def print_len(self):
        print("length of a password",len(self.__password))
pwd=Password("hacker@123")
pwd.print_len()
output=pwd.get_password()
print(output)
pwd.set_password("pramod@1123")
pwd.print_len()