class User:
    def __init__(self,f_name,l_name) -> None:
        self.first = f_name
        self.last = l_name
        self.email = f'{self.first}.{self.last}@user.com'
    
    @property
    def full_name (self):
        return f'{self.first} {self.last}'
    
    @full_name.setter 
    def full_name(self,value): #setter
        first , last = value.split(' ')
        # self.first = value.split(' ')[0]
        # self.last = value.split(' ')[1]
        self.first = first
        self.last = last
        self.email = f'{first}.{last}@user.com'
        pass

    def get_email (self):
        return self.email 

mark = User("mark",'zuku')
print(mark.first)
print(mark.last)
print(mark.email)
print(mark.get_email())

# setter
mark.full_name = "Hamid Hosen"
print(mark.full_name)
print(mark.email)

print(mark.first)
print(mark.last)
print(mark.email)