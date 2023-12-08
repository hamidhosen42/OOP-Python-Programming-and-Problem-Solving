
# ! Principles of Object-Oriented Programming Abstract Class

# !Abstraction refers to using simplified classes, rather than complex implementation code, to access objects. Often, it's easier to design a program when you can separate the interface of a class from its implementation. In OOP, you can abstract the implementation details of a class and present a clean, easy-to-use interface through the class member functions. Abstraction helps isolate the impact of changes made to the code so if an error occurs, the change only affects the implementation details of a class and not the outside code.

#! Introduction to Interface in Python. An interface acts as a template for designing classes. Interfaces also define methods the same as classes, but abstract methods, whereas class contains nonabstract methods. Abstract methods are those methods without implementation or which are without the body.

# ! This is a simple example of an abstract class in Python.

from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def move(self):
        print("moving around ........")

class Monkey(Animal):
    def __init__(self) -> None:
        self.__name = "Hamid Hosen"

    def sign(self):
        print("Monkey is signing")

    def eat(self):
        print("Eating Banana")

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name = value

    def move(self):
        print("dskkdfskkdf ...........")
        return super().move()

class Tiger(Animal):
    def eat(self):
        pass

    def move(self):
        pass

hamid = Monkey()
print(hamid)
hamid.eat()
hamid.move()
hamid.name = "Azad"
print(hamid.name)