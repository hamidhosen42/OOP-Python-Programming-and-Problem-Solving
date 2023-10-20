numbers = [12,13,24,5345,35,3,45,2,1]
numbers_iter = iter(numbers)
print(numbers_iter)

try:
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    
    print("Hi ,")
    print("How are you ,")
    
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    
    print("Hi ,")
    print("How are you ,")
    
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))

except StopIteration:
    print("Stop Iteration")