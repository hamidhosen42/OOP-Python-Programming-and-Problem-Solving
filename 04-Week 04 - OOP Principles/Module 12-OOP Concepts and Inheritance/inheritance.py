
#! Inheritance
#! Base class will have only the common attribute
class Devices:
    def __init__(self,brand,price,color) -> None:
        self.brand = brand
        self.price = price
        self.color = color

    def re_sale(self):
        print("Ready to sell again")
 
class Laptop(Devices):
    def __init__(self,brand,price,color,disc_size) -> None:
        super().__init__(brand,price,color)
        self.disc_size = disc_size

    def run (self):
        print("Running the laptop")

    def __repr__(self) -> str:
        return f'Laptop {self.brand} : {self.price}: {self.color}'
    
    def purchase(self,money,discount):
        if money < (self.price - self.price * discount/100):
            return "No Laptop for you"
        else:
            print( "You can buy the laptop")
            return money-self.price
        
class Phone(Devices):
    def __init__(self,brand,price,color,camera,sim_num) -> None:
        super().__init__(brand,price,color)
        self.camera = camera
        self.sim_num = sim_num

    def __repr__(self) -> str:
        return f'Phone {self.brand} : {self.price}: {self.color} : {self.camera} : {self.sim_num}'

    def is_dual_sim(self):
        return self.sim_num>1
    
    def purchase(self,money):
        if money < self.price:
            return "No Laptop for you"
        else:
            print( "You can buy the laptop")
            return money-self.price

class Watch:
    def __init__(self,brand,price,color,watch_type) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.watch_type = watch_type
        
    def is_digital(self):
        return self.watch_type == "digital"
    
    def purchase(self,money):
        if money < self.price:
            return "No Laptop for you"
        else:
            print( "You can buy the laptop")
            return money-self.price
    
class Manager:
    def __init__(self,name,salary,experience,designation) -> None:
        pass

    def withdraw_salary(self):
        pass

    def day_total_sales(self):
        pass

    def handle_cutomer_complaine(self):
        pass

class SalesPerson:
    def __init__(self,name,salary,experience,designation,connission) -> None:
        pass

    def withdraw_salary(self):
        pass

    def handle_customer(self):
        pass

acer = Laptop("Acer",85000,'black','500gb')
hp = Laptop("hp",60000,'silver','250gb')

print(acer)
print(hp)

apple = Phone("Apple",15000,'black',"15mp",2)
oppo = Phone("oppo",15000,'silver',"12mp",1)
print(apple)
print(oppo)

hp.re_sale()
print(hp.brand)

print(apple.brand)