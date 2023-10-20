# def squre(x):
#     return x*x

squre = lambda x: x*x

result = squre(6)
print(result)

add = lambda x,y:x+y
print(add(4,5))

num=[2,3,4,5,56,56,8634,3,4,5563,5363]

mul=lambda x:x*2

# num2=map(mul,num)
# print(list(num2))

num2 = map(lambda x:x*2,num)
print(list(num2))