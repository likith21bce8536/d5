class BankAccountSbi:
    bankname="sbi"#class variable
    def __init__(self):
        pass


class SavingsAccount(BankAccountSbi):
    accounttype="savings"#inner class variable
    def __init__(self):
        self.accountholdername="likith"
        self.__accountnumber='12345667'
        self.__minbalance=50000
        self.__pin="1234"

    def pin_check(self,pin):
        return pin == self.__pin #return true

    def details(self):
        print(f"{self.accountholdername} is account holder with bank account {self.__accountnumber} and having min balance of {self.__minbalance}")


    def deposite(self,d_amount,pin):
        if self.pin_check(pin):

            self.__minbalance+=d_amount
            print("the amount has been added")
        else:
            print("pin is incorrect")


    def withdraw(self,w_amount,pin):
        if self.pin_check(pin):
            if self.__minbalance < w_amount:
                print("insufficient balance")
            else:
                self.__minbalance-=w_amount
                print("the amount is withdraw")

    def check_bal(self,pin):
        if self.pin_check(pin):
            print(f"your main baolance is :- {self.__minbalance}")
        else:
            print("invalid pin")





sobj=SavingsAccount()
#d_amount=int(input("enter the amount to deposite:-"))
#w_amount=int(input("enter the amount to withdraw:-"))
pin=input("enter the pin:-")
#sobj.deposite(d_amount,pin)
#sobj.withdraw(w_amount,pin)
sobj.check_bal(pin)
sobj.details()