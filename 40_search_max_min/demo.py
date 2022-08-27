
def search(iter, value):
    for number in iter:
        if number == value:
            return True
    return False

def getmax(iter):
    currmax = iter[0]
    for item in iter[1:]:
        if(item > currmax):
            currmax = item
    return currmax

def getmin(iter):
    pass

if __name__ == '__main__':


    import random
    iter = [random.randint(1, 100) for i in range(100)]

    print('Testing search()')

    searchvalue = 45    
    print(search(iter, searchvalue))

    searchvalue = 101    
    print(search(iter, searchvalue))

    results = []
    for i in range(1, 101):
        searchvalue = i    
        results.append(search(iter, searchvalue))
    print(sum(results))

    print('Testing getmax()')

    testlist = list(range(1, 100)) 
    print(getmax(testlist))
    print(getmax(iter))