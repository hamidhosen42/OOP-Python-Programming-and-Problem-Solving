class User:
    def __init__(self,name,password,phone):
        self.name = name
        self.__password = password
        self.phone = phone

    def __get_password(self):
        print(self.__password)

    def user_login(self,name,password):
        if (name == self.name and password == self.__password):
            return True
        return False

name = User("Hamid","21121","w2323424")
# print(name.__password)
# print(name.phone)

# name.get_password()

print(name.user_login("Hamid","21121"))