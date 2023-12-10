import json

class Item:
    all = []
    def __init__(self,name,price) -> None:
        self.name = name
        self.price = price
        self.all.append(self)

    @staticmethod
    def initialize():
        with open('extract.txt','r') as file:
            data = file.read()
            js = json.loads(data)
        
        for item in js:
            print(item)
            Item(item['name'],item['price'])

    def __repr__(self) -> str:
        return f"Item({self.name},{self.price})"
            
Item.initialize()
print(Item.all)