#create a class called bank account
import time;

class bankaccount:
    
    def __init__(self,account_number,balance,date_of_opening,customer_name):
        self.account_number=account_number
        self.balance=balance
        self.date_of_opening=date_of_opening
        self.customer_name=customer_name
    def deposit(self):
         self.deposit=float(input("enter your deposit:"))
         self.balance=self.balance+self.deposit
         print("",self.deposit)
         return self.deposit
    def withdraw(self):
        
        if self.balance>0:
            self.withdraw=float(input("enter amount to withdraw"))
            self.balance=self.deposit-self.withdraw
            print("you have withdrawn:",self.withdraw)
        else:
            print("balance is less than 0")
        return self.withdraw
    def check_balance(self):
        self.balance=self.deposit-self.withdraw
        print("your account balance is:",self.balance)
        return self.balance
    def customer_details(self):
        account_number=input("enter your account number:")
        customer_name=input("enter your customer name:")
        date_of_opening=time.asctime()
        print("",account_number)
        print("",customer_name)
        print("date",date_of_opening)

cust1=bankaccount(0,0,4,'m')
cust1.customer_details()
cust1.deposit()
cust1.withdraw()
cust1.check_balance()

          

