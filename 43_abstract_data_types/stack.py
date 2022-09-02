class Stack(object):

    def __init__(self, size=10):
        self._maxsize = size
        self._size = 0
        self._buffer = []

    def push(self, dataunit):
        if(self._size <= self._maxsize):
            self._buffer.append(dataunit)
            self._size += 1

    def pop(self):
        if(self._size > -1):
            self._size -= 1
            return self._buffer.pop()

    def getsize(self):
        return self._size


# ----------------------------------------------

s = Stack(5)
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

for i in range(s.getsize()):
    print(s.pop(), end = ' ')


