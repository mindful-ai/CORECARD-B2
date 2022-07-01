# write a function to get the span of substrings in a string

''' 
    input main mississippi
    input substr ss
    output (2, 4), (5, 7)
'''


def getspan(substr, string):
    temp = string
    pointer = 0
    spans = []
    while substr in temp:
        start = temp.find(substr) + pointer
        end = start + len(substr)
        spans.append((start, end))
        pointer = start + 1
        temp = string[pointer:]
    return tuple(spans)

if __name__ == '__main__':

    # inputs

    main = input("Enter main text: ")
    substr = input("Enter substring: " )

    # process

    spans = getspan(substr, main)

    # output

    print(spans)

