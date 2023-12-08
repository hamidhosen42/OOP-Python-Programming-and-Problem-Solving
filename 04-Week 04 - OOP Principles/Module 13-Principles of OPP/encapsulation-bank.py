
# !Principles of Object-Oriented Programming 

#! Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.

class Account:
    def __init__(self,holder,initial_balance):
        self.holder = holder #! public attribute
        self._acount_number = 165
        self.__balance = initial_balance #!private

    def deposite(self,amount):
        print(f'Adding{amount} to your account')
        self.__balance += amount

    def withdraw(self,amount):
        print(f'Withdrawing {amount} to your account')
        self.__balance -= amount

class StudentAccount(Account):
    def __init__(self,holder,initial_balance,school):
        self.school = school
        super().__init__(holder,initial_balance)

    def get_balance(self):
        return self._acount_number


hamid = StudentAccount("Hamid",2330,"EDU")
# print(hamid.__balance)

hamid.deposite(100)
# print(hamid.__balance)

hamid.withdraw(50)
# print(hamid.__balance)

print(hamid._acount_number)