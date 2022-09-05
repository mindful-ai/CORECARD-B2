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

start = root
start.data = 100
print(start.data, root.data)

# if I change start, root also changes because the refereces are copied
# to over come the problem we use a function called deepcopy

from copy import deepcopy
start = deepcopy(root)
start.data = 200
print(start.data, root.data)

def traverse(beginptr):
    temp = beginptr
    while temp.link != None:
        print(temp.data, end=' ')
        temp = temp.link

def find(beginptr, value):
    temp = beginptr
    while temp.link != None:
        if(temp.data == value):
            return True
        temp = temp.link
    return False

# -------------------------------------------------- Testing functions

if __name__ == '__main__':

    traverse(root)

    print(find(root, 10))
    print(find(root, 30))





