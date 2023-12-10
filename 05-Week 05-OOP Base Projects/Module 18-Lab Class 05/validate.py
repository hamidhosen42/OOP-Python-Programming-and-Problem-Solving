class Person:
    def __init__(self,name,phone,age) -> None:
        assert age>13, f"Only greater than 13 is accepted"
        assert len(phone)==11, f"Invalid phone no"
        self.name=name
        self.phone=phone
        self.age=age
    def __repr__(self) -> str:
        return f"{self.name} {self.phone} {self.age}"
    
user = Person("Rakibullah","01234567893",15)
print(user)