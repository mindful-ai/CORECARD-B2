class queue(object):

    def __init__(self, size=10):
        pass

    def get():
        pass

    def put():
        pass

    def getsize():
        pass

# ----------------------------------------------

q = Queue(5)
q.put(10)
q.put(20)
q.put(30)
q.put(40)
q.put(50)

for i in range(q.getsize()):
    print(q.get(), end = ' ')