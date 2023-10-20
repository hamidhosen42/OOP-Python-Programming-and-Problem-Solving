number = [12,45,65,23,89,78,11]
names = ['hamid','hosen','fahim']
ages=[22,23,45]

odd_number = []
for num in number:
    if num%2==1:
        odd_number.append(num)
# print(odd_number)

odd_number1 = [num for num in number if num%2==1] 
print(odd_number1)

odd_number2 = [num for num in number if num%2==1 if num%5==0] 
print(odd_number2)

pairs =[(name,age) for name in names for age in ages if age<25]
print(pairs)

for name in names:
    print(name)

    for age in ages:
        if age<25:
            print(name,age)