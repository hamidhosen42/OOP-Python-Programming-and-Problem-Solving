class Bank:
     def __init__(self,balance):
          self.balance = balance
          self.min_withdraw = 100
          self.max_withdraw = 10000

     def get_balance(self):
          return self.balance
     
     def withdraw(self,amount):
          if amount<self.min_withdraw:
               return 'no money for you'
          elif amount>self.max_withdraw:
               return f'you crossed max limit: {self.max_withdraw}'
          elif amount>self.balance:
               return 'you are broke!!! No money for you'
          else:
               self.balance=self.balance-amount
               return f'Here is your money: {amount}'
          
     def deposite(self,amout):
          self.balance = self.balance+amout
          
my_bank = Bank(8000)
print(my_bank.withdraw(10))
print(my_bank.withdraw(100000))
print(my_bank.withdraw(9000))

my_bank.withdraw(1000)
print(my_bank.balance)
#or
print(my_bank.get_balance())

my_bank.deposite(2000)
print(my_bank.get_balance())