numbers = [12,13,24,5345,35,3,45,2,1]
  
def get_number(nums):

    for num in nums:
        yield num

result = get_number(numbers)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print("Hi,")
print("Hi,")
print("Hi,")
print(next(result))
print(next(result))
print(next(result))
print(next(result))