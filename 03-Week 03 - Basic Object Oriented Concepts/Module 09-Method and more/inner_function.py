def do_something():
    print("Insite the function do_something")

    def inner_function():
        print("Insite the inner function")

    inner_function()

# do_something()

def first_function():
    print("Insite the first function")

    def second_function():
        print("Insite the inner function")

    return second_function

# first = first_function()
# print(first)

first_function()()