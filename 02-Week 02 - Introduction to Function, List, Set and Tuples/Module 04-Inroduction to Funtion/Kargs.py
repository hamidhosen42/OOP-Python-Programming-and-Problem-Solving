# def add(num1,num2,*num):
#     print(num1)
#     print(num2)
#     print(num)
    
# add(2,3,4,5)

def full_name(f_name,l_name):
    name = f'{f_name} {l_name}'
    return name

name = full_name(l_name='Hosen',f_name='Hamid')
# print(name)

def long_name(**kargs):
    print(kargs)

name1 = long_name(first='Dr',last="Chowdhury",middle = 'Rahman')
# print(name1)


def name_mixed(first,second,**name_parts):
    print(first,second,name_parts)

name2 = name_mixed(first='Chowdhury',second="Fahim",middle = 'majari')
print(name2)

def all_types (first,*args,**kargs):
    print(first)
    # print(args)
    for i in args:
        print(i)

    # print(kargs)
    for key,value in kargs.items():
        print(key,value)

all_types('abc','ddd','kjk','lll','pp',name="sdfasdf",father="sdsf")