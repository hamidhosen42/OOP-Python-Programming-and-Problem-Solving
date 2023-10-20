def add(num1,num2):
    total=num1+num2
    print(f'num1: {num1} and num2: {num2}')
    return total

# result = add(12,14)
# result = add(num2=12,num1=14)
# print(result)

def multiply(num1,num2=1):
    result = num1 * num2
    return result

output = multiply(45,2)
# print(output)

def multiply2(*number): # args
    result = 1
    for num in number:
        result = result + num
        # print(num)
    return result

final_result = multiply2(12,3,3,4,5)
print(final_result)