# def do_something(x,y):
#     print(f'x: {x} y: {y}')


# do_something(23,45);
# do_something("Hamid","Hosen")

def do_something(work):

    print("Start Work")
    # print(work)
    work()
    print("Done Work")

def practice_coding():
    print("I am  practicing Python")

def learning_python():
    print('Learning python class')

do_something(practice_coding)
do_something(learning_python)