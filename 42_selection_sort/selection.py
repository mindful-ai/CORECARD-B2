# Implementation
def selection(iter, asc=True):
    temp = iter
    for i in range(0, len(iter)):
        startindex = i
        for j in range(startindex + 1, len(iter)):
            if(temp[startindex] > temp[j]):
                t = temp[startindex]
                temp[startindex] = temp[j]
                temp[j] = t
    return temp



# Test the algorithm
if __name__ == '__main__':

    print(selection([9, 1, 3, 5, 7, 8, 2, 4, 6, 6, 6]))  # 1, 2, 3, 4
    print(selection([4, 1, 3, 2])) # 4, 3, 2, 1
    print(selection([4, 1, 3, 2], asc=False)) # 4, 3, 2, 1