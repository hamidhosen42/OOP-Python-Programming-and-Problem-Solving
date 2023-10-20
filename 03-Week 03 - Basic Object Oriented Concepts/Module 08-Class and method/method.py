def add (a,b):
    sum = a+b
    print(sum)

def deduct(x,y):
    result  = x-y
    return result

class Phone:
    brand = "Samsung"
    color = "Black"
    price = 25000
    features = ['camera','water proofs','can be used as a hammer']

    def call(self):
        print("lorem")

    def send_sms(self,number,text):
        sms =  f"sending sms {text} to {number}"
        return sms

my_phone = Phone()
# print(my_phone.call())

sms = my_phone.send_sms("2342342","sdfsasdfa asdfa")
print(sms)

print(my_phone.call())