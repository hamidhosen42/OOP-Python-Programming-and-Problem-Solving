
#! Introduction to Python method overriding and operator overloading

def add(n1,n2,n3=0):
    return n1+n2

print(add(2,3))

def add1(*args,**kwargs):
    print("Args: ", args)