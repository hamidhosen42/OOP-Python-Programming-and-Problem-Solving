class Shopper:
    def __init__(self,name):
        self.name = name
        self.cart = []
    
    def add_to_cart(self,item,price,quantity):
        self.cart.append({'item':item,'price':price,'quantity':quantity})

    def checkout(self,amount):
        # print(self.cart)
        price = 0
        for item in self.cart:
            print(item)
            price = price + item['price'] * item['quantity']
        print(price)
        if amount < price:
            return f'Please give me more money: {price - amount}'
        elif amount > price: 
            return f'Here are the items and extra money: {amount - price}'
        else:
            return 'Here are the items'

shopping = Shopper('Bag Tan')
shopping.add_to_cart('shirt', 400, 3)
shopping.add_to_cart('shoes', 899, 4)
shopping.add_to_cart('pant', 1400, 2)

print(shopping.checkout(8000))