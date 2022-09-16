def search(string, substr):

    length = len(substr)
    start = 0
    end = length

    indeces = []
    while end <= len(string):
        #print(string[start:end])
        if(string[start:end] == substr):
            indeces.append((start, end))
        start += 1
        end += 1

    return indeces


if __name__ == "__main__":

    s = "FFDFKAJKLJFSFSDFFDFFFSDOIRKFFDSLKDDFFFJGFFDKFFFD"
    ss = "FFD"
    print(search(s, ss))