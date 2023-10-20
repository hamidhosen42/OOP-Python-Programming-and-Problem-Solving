from math import sin,ceil
import random
from datetime import datetime as d

result = sin(30)
print(result)

result1 = ceil(2.34)
print(result1)

num = random.random()
print(num)

num1 = random.randint(30,40)
print(num1)

winner = random.choice([2,3,34,5,67,85,45])
print(winner)

date = d.now()
print(date.strftime("%Y-%m-%d %H:%M:%S")) 