class Laptop:
    def __init__(self,brand,age):
         self.brand = brand
         self.age = age

    def increase_age(self,age=1):
         self.last_age = self.age
         self.age = self.age+age

    def repair(self,life_increase=5):
         self.increase_age(-5)

my_leptop = Laptop("acer",23)
my_leptop.increase_age()
print(my_leptop.age)
my_leptop.age = 50
my_leptop.increase_age()
print(my_leptop.age)
print(my_leptop.brand)
print(my_leptop.last_age)
my_leptop.repair(-10)
print(my_leptop.age)
print(my_leptop.__dict__)