class Bus:
    owner = "Ena Transport"

    def __init__(self,route,license,driver) -> None:
        self.route = route
        self.license = license
        self.driver = driver
        self.trips = []
        
    def start_trip(self,start_time):
        self.trips.append(start_time)

class Driver:
    def __init__(self,name,mobile,license,address,salary) -> None:
        pass

    def drive(self,start,end):
        pass

    def take_vacation(self):
        pass

    def withdraw_saary(self):
        pass

class Passenger:
    def __init__(self,name,mobile,destination) -> None:
        pass

    def purchase_ticket(self,destination,money):
        pass

class Manager:
    def __init__(self,name,mobile,department) -> None:
        pass

class Counter :
    def __init__(self,manager) -> None:
        pass