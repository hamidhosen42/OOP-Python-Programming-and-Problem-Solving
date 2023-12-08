
# ! Access Modifier private public and protected

class Account:
    def __init__(self,holder) -> None:
        self._account_holder = holder
    pass

class StudentAccount(Account):
    def __init__(self,holder,balance,school):
        self.__balance = balance

    def deposite(self,amount):
        if amount<0:
            return "Negative amount can not added"
        print(f'Adding{amount} to your account')
        self.__balance += amount

    def withdraw(self,amount):
        if amount>self.__balance:
            return "Insufficient Balance"
        print(f'Withdrawing {amount} to your account')
        self.__balance -= amount
        return amount

    def get_balance(self):
        return self.__balance
    
hamid = StudentAccount("Hamid Hosen",12000,"EDU")
hamid.deposite(100)
print(hamid.get_balance())
print(hamid._StudentAccount__balance)
# print(dir(hamid))

