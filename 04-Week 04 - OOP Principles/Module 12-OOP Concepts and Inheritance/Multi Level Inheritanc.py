
#! Multi Level  Hierarcy with Vehicle Management

class Vehicle:
    def __init__(self,name,license,price) -> None:
        self.name = name
        self.license = license
        self.price = price

    def start(self):
        print(f"{self.name} started")

class Bus(Vehicle):
    def __init__(self, name, license, price,seat,ticket_price) -> None:
        super().__init__(name, license, price)
        self.seat = seat
        self.available_seats = seat
        self.ticket_price = ticket_price

    def sell_ticket(self,customer_name,quantity,amount):
        self.available_seats -= quantity
        remainer = amount - self.ticket_price * quantity
        if remainer >=0:
            return  Ticket(customer_name)
        else:
            return "No ticket for you"
        
class AcBus(Bus):
    def __init__(self, name, license, price, seat, ticket_price) -> None:
        super().__init__(name, license, price, seat, ticket_price)
        print('This is ac bus bus')

class MiniBus(Bus):
    def __init__(self, name, license, price, seat, ticket_price) -> None:
        super().__init__(name, license, price, seat, ticket_price)
        print('This is mini bus')
        
class Ticket:
    def __init__(self,owner) -> None:
        self.owner = owner

mini = MiniBus("S Alam","232","34",4,230)
print(mini.name)