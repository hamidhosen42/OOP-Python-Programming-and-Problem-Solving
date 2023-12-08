
# !Principles Of Object-Oriented Programming Polymorphism

#! poly => many
#! morph => different

#! Introduction to Python method overriding and operator overloading

class Animal:
    def __init__(self,name) -> None:
        self.name = name

    def make_sound(self):
        print("Animal making some sound")

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print("Animal making")

class Dog(Animal):
    def __init__(self, name) -> None:
        Animal.__init__(self,name)
    
    def make_sound(self):
        print(" making")

don = Cat("don")
don.make_sound()

wow = Dog("ssdsd")
wow.make_sound()