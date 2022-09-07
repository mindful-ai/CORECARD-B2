from copy import deepcopy
class dataunit(object):

    def __init__(self, data):
        self.data = data
        self.link = None

    def setdata(self, data):
        self.data = data
    
    def getdata(self):
        return self.data

    def setlink(self, link):
        self.link = link

    def getlink(self):
        return self.link


# -----------------------------------------------------

d1 = dataunit(10)
print(d1)
print(d1.data, d1.link)
d2 = dataunit(20)
d1.link = d2
print(d1.data, d1.link)

# -----------------------------------------------------

d1 = dataunit(10)
d2 = dataunit(20)
d3 = dataunit(30)
d4 = dataunit(40)
d5 = dataunit(50)

# 10 -> 20 -> 30 -> 40 -> 50 -> None

d1.link = d2 # d1.setlink(d2)
d2.link = d3
d3.link = d4
d4.link = d5
d5.link = None
root = d1

# ------------------------ Traversing a linked list

'''
start = root
start.data = 100
print(start.data, root.data)

# if I change start, root also changes because the refereces are copied
# to over come the problem we use a function called deepcopy

from copy import deepcopy
start = deepcopy(root)
start.data = 200
print(start.data, root.data)
'''

def traverse(beginptr):
    temp = beginptr
    while temp != None:
        print(temp.data, end=' ')
        temp = temp.link
    print("\n")

def find(beginptr, value):
    temp = beginptr
    while temp.link != None:
        if(temp.data == value):
            return True
        temp = temp.link
    return False

def insert(head, pos, dataunit):  # 0, -1, 1, 2, 3, 4, 5 ...
    temp = dataunit
    curr = head
    count = 0
    global root
    if pos == 0:
        temp.setlink(head)
        root = temp
    elif pos == -1:
        while curr.getlink() != None:
            curr = curr.link
        curr.link = temp
    else:
        while count < pos - 1:
            curr = curr.link
            if(curr.link == None):
                break
            count += 1
        temp.setlink(curr.link)
        curr.setlink(temp)

# Assignments       
def delete(start, pos):
    pass

def reverse():
    global root
    prev = deepcopy(root)
    prev.setlink(None)
    curr = deepcopy(root.getlink())
    pointer = deepcopy(root.getlink())
    while True:
        print(prev.getdata(), curr.getdata())
        curr.setlink(prev)
        prev = deepcopy(curr)
        curr = deepcopy(pointer.getlink())
        pointer = pointer.getlink()
        if(curr.getlink() == None):
            curr.setlink(prev)
            break
    print(curr.getdata())
    root = deepcopy(curr)

# Swappig of two nodes
# Adjecent nodes only
def swap(a, b):
    global root
    if(a == 0):
        temp = root
        root = root.getlink()
        temp.setlink(root.getlink())
        root.setlink(temp)
    else:
        x = root
        c = 0
        while c < a - 1:
            x = x.getlink()
            c += 1

        prev = x
        curr = x.getlink()
        print(prev.getdata(), curr.getdata())

        temp = curr
        prev.setlink(curr.getlink())
        temp.setlink(temp.getlink().getlink())
        prev.getlink().setlink(temp)


def swapany(a, b):
    pass

def bubble(start):
    pass

# -------------------------------------------------- Testing functions

if __name__ == '__main__':

    print('Starting tests....\n')
    traverse(root)
    
    ''' 
    print(find(root, 10))
    print(find(root, 30))

    insert(root, 0, dataunit(1))
    print('\n---------------------------------\n')
    traverse(root)

    insert(root, -1, dataunit(50))
    print('\n---------------------------------\n')
    traverse(root)

    insert(root, 3, dataunit(78))
    print('\n---------------------------------\n')
    traverse(root)
    
    reverse()
    print('\n---------------------------------\n')
    traverse(root)
    '''
    swap(0, 1)
    print('\n---------------------------------\n')
    traverse(root)

    swap(3, 4)
    print('\n---------------------------------\n')
    traverse(root)