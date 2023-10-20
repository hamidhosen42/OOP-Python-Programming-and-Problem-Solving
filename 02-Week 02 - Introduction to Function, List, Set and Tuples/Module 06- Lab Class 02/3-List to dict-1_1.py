my_list = ["apple", "banana", "cherry", "apple", "cherry"]

output_dict = {}

for index,val in enumerate(my_list):
    # print(index,val)
    if val[0]=="a":
        output_dict[val] = my_list[index+1]

print(output_dict)