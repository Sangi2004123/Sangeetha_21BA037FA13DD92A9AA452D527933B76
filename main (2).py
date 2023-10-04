class BankAccount:
  def__intit__(self,account_number, account_holder_name,initial_balance=0.0):  
self.__account_number=account_numberself.__account_holder_name=account_holder_name
self.__account_balance=initial_balance
 def deposit (self,amount):
    if amount>0:
      self.__account_balance+=amount
#self.__acconut_balance=self.__account_balance+account
    print("Deposited ₹{}.New balance:₹{}.format(amount,self.__account_balance)) 
   else:
    print("Invalid deposit amount.")
  def Withdraw(self, amount):
    if amount >0 and amount<=self.__account_balance:
      self.__account_balance=self.__account__balance_=amonunt
#self.__account_balance=self.__account_balance_amount
   print("Withdraw ₹{}.New balance:₹{}".format(amount,self.__account_balance))
else:
  print("Invalid Withdrawal amount or insufficient balance.")
  def display_balance(self):
    print("account balance for {}(account #{}:₹{}".format(self.__account_holder_name, self.__account_number,self.__account_balance))
#create an instance of the Bank Account class
account=BankAccount(account_number="123456789"acount_holder_name="Sangeetha",initial_balance=5000.0)
#Test deposit and withdraw functionality
account.display_balance()
account.deposit(500.0)
account.withraw(200.0)
account.withraw(200.0)
amount.display_balance()
               