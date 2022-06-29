# Program to print all the factors of a number

'''
INPUT 10
OUTPUT 1, 2, 5, 10
'''

# input
n = int(input("Enter a number: "))

# process
factors = []
for i in range(1, n+1):
    if(n % i == 0):
        factors.append(i)

# output

print(factors)
