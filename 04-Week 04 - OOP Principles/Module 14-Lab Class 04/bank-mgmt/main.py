
# !"""Manages Bank Account"""

class Account:
    accID = 1

    def __init__(self, name,age,nid_num, balance):
        self.name = name
        self.age = age
        self.nid_num = nid_num
        self.balance = balance

        #! update acc id
        self.account_id =Account.accID
        Account.accID+=1

    def deposite(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

acc_1 = Account("Hamid Hosen",24,600,500)
acc_2 = Account("Hamid Hosen1",25,700,600)

print("------------------Deposite--------------------")
print("First Account:",acc_1.account_id)
acc_1.deposite(500)
print("First Account Deposite Balance,",acc_1.balance)
acc_1.withdraw(100)
print("First Account Withdraw Balance,",acc_1.balance)

print("------------------Withdraw--------------------")
print("Second Account:",acc_2.account_id)
acc_2.deposite(500)
print("Second Account Deposite Balance,",acc_2.balance)
acc_2.withdraw(100)
print("Second Account Withdraw Balance,",acc_2.balance)