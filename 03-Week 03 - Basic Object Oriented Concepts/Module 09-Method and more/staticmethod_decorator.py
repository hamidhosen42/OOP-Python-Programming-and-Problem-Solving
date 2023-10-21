class Shopping:
    def __init__(self,customer):
        self.customer = customer
        self.items = []
        self.total = 0

    @staticmethod
    def multiply(x,y):
        return x * y
    
    def add_to_total (self,amount):
        self.total +=amount

    def add_to_card(self,item,price,quantity):
        self.items.append(item)
        item_total = price * quantity
        self.add_to_total(item_total)
        # self.total += item_total

    def checkout(self):
        pass

result = Shopping.multiply(45,5)
print(result)

# result_2 = Shopping.add_to_card(34)
my_shopping = Shopping("Hamid Hosen")
my_shopping.add_to_total(200)
print(my_shopping.total)

my_shopping.add_to_total(200)
print(my_shopping.total)

my_shopping.add_to_card("Apple",100,3)
print(my_shopping.items)
print(my_shopping.total)

print(my_shopping.multiply(2,3))