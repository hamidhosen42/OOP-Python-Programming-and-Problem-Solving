class Phone():

    manufactured = "china"

    def __init__(self,brand,price,color):
        self.brand = brand
        self.price = price
        self.color = color

    def send_sms(self,number,text):
        sms =  f"sending sms {text} to {number}"
        return 
    
my_phone = Phone("Apple",1242423,"Black")
print(my_phone.brand)
print(my_phone.price)
print(my_phone.color)


my_phone1 = Phone("APPO",1242423,"Black")
print(my_phone1.brand)
print(my_phone1.price)
print(my_phone1.color)