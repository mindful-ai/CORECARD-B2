# Program to print a character triangle

'''
N = 3
C = #

OUTPUT

#
##
###

'''

# input
N = int(input("Enter number of lines: "))
C = input("Enter the character:")

# process
# output

for i in range(N + 1):
    print(C * i, end='')
    print("")

    
