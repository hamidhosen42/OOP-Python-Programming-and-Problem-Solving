from functools import partial

def get_number(a,b,c,d):
    return a*1000+b*100+c*10+d

number = get_number(2,3,4,5)
fourth_only = partial(get_number,b=0,c=0,d=0)
number2 = fourth_only(23)
print(number2)
