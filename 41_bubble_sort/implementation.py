def bubble(iter, asc=True):
    temp = iter
    swap = -1
    while swap != 0:
        i = 0
        j = 1
        swap = 0
        while True:
            if(asc==True):
                if(temp[i] > temp[j]):
                    t  = iter[i]
                    iter[i] = iter[j]
                    iter[j] = t 
                    swap += 1
            else:
                if(temp[i] < temp[j]):
                    t  = iter[i]
                    iter[i] = iter[j]
                    iter[j] = t 
                    swap += 1
            i += 1
            j += 1
            if(j == len(temp)):
                break
    return temp

if __name__ == '__main__':

    print(bubble([4, 2, 1, 3]))
    print(bubble([4, 2, 1, 3], asc=False))