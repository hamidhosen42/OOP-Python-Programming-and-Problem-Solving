class Shop:

    cart=[]

    def __init__(self,buyer):
        self.buyer = buyer

    def add_to_cart(self,item):
        self.cart.append(item)

shopping1 = Shop("Hamid Hosen")
shopping1.add_to_cart("T-Shirt")
print(shopping1.cart)

shopping2 = Shop("Fahim")
shopping2.add_to_cart("Shoes")
print(shopping2.cart)