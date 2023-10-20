# def timer(func):

#     def inner():
#         print("Inner function")
#         func()
#         print("Time Function")
#     return inner()

# def get_function():
#     print("Function")

# timer(get_function)

# !========================

# def timer(func):

#     def inner():
#         print("Inner function")
#         func()
#         print("Time Function")
#     return inner

# def get_function():
#     print("Function")

# timer(get_function)()

# ! A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.

import math
import time
def timer(func):

    def inner( *arge,**kwargs):
        print("Inner function")
        start = time.time()
        func(*arge,**kwargs)
        end = time.time()
        print("Time Function: ",end-start)
    return inner

@timer
def get_function(n):
    result = math.factorial(n)

    print(f"Factorial of {n} is : {result}")
    # print("Function")

get_function(n=3)