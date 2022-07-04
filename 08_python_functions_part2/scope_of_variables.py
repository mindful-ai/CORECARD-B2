a = 20 # Global variable

def func1():
    print("(func1)The value of a is ", a)

def func2():
    a = 10 # Local to func2
    print("(func2)The value of a is ", a)

def func3():
    a = 10 # Local to func3
    def func():
        a = 5
        print("(func3:func)The value of a is ", a)
    func()

def func4():
    a = 10 # Local to func3, nonlocal to func
    def func():
        global a
        print("(func3:func)The value of a is ", a)
    func()

def func5():
    a = 10 # Local to func3, nonlocal to func
    def func():
        nonlocal a
        print("(func3:func)The value of a is ", a)
    func()

func1()
func2()
func3()
func4()
func5()