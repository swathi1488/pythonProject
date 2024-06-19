class Bank_account:
    def __init__(self):
        self.balance=0
    def deposite(self,amount):#public function
        self.balance +=amount
    def _withdraw(self,amount):#protected
        self.balance -=amount
    def __show_balance(self):#private
        print("your balance is",self.balance)

    def is_auth_True(self,isAuth):
        if isAuth:
         self.__show_balance()
        else:
         print("your not  authonticate")

    def do_withdraw_by_manager(self,amount):
        self._withdraw(amount=amount)



hdfc=Bank_account()
hdfc.deposite(1000)
hdfc._withdraw(499)#not good practice
#hdfc.__show_balance()#error
hdfc.is_auth_True(True )
#hdfc.is_auth_True(False)
