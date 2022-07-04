def average(a, b, c):
    return (a + b + c) / 3

def average2(*targs):
    print(targs)

def func(**kargs):
    print(kargs)

def func2(a, b, c, *targs, **kargs):
    print(a, b, c) # required arguments
    print(targs) # tuble arguments
    print(kargs) # keyword arguments

def show(message="Hello"):  # specifying default arguments
    print("message is ", message)

print(average(1, 2, 3))

average2(1, 2, 3, 4, 5)

func(name='anil', age=35, company='corecard')

func2(3, 4, 5, 6, 7, name='anil') # order should be like this only

show()
show("This is a new message")