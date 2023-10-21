class Shopping:
    mall = "New Market"
    hour = []

    def __init__(self,customer):
        self.customer = customer
        self.items = []
        self.total = 0

    def opening_hout(cls, day):
        return cls.mall

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