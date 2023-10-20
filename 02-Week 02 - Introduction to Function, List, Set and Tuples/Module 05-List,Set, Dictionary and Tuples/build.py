largest =max(2,342,343,1,34,4)
numbers = [12,13,24,5345,35,3,45]
number = {12,34,35,6,7,8,43}
big_num = max(number)

print(big_num)

number_rev = reversed(numbers)
print(list(number_rev))

sorted_numbers =sorted(numbers,reverse=True)
print(sorted_numbers)

actor =[
    {'name':'Hamid','age':22},
    {'name':'Hamid1','age':23},
    {'name':'Hamid2','age':24},
    {'name':'Hamid3','age':25},
    {'name':'Hamid4','age':26},
]

sorted_actor = sorted(actor,key=lambda actor:actor['age'],reverse=True)
print(sorted_actor)