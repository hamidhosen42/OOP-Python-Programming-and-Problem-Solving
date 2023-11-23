What are the dunder (magic) methods in Python?
 A Methods that start with a double underscore. 
B Methods that start and end with a double underscore 
C Methods that start with a single underscore 
D Methods that start and end with a single underscore 

What is true about the __init__() method? 
A It is a constructor 
B It is a magic method 
C It calls __new__() method 
D All of the above

What symbol is used to decorate a function?
 !
 +
 @
 /
 4. Decorators do not modify a function ______.
 Permanently
 Temporarily
 Can not be determined
 None of the above

5.Which of the following statement(s) is/are true?
Statement 1: Nested functions are functions that are defined inside another function
Statement 2: Nested functions can access variables of the enclosing scope
 Statement 1 is true
 Statement 2 is true
 Both statements are true
 None of the statements are true
 6. : How to define a static method in Python? 
A Using static() function 
B Using @staticmethod decorator 
C using @classmethod decorator 
D Can't define a static method in Python 
7.  All the members of the class are _______ by default. 
A Public 
B Private 
C Protected 
D Internal
8. class Fruit:
pass
   print(Fruit.__name__)
 
 class
 __main__
 AttributeError
 Fruit
9. In the following Python code, which function is the decorator?
def mk(x):
    def mk1():
        print("Decorated")
        x()
    return mk1
def mk2():
    print("Ordinary")
p = mk(mk2)
p()

a) p()
b) mk()
c) mk1()
d) mk2()

Explanation: In the code shown above, the function mk() is the decorator. The function which is getting decorated is mk2(). The return function is given the name p().

10. A function with parameters cannot be decorated.
a) True
b) False
Explanation: Any function, irrespective of whether or not it has parameters can be decorated. Hence the statement is false