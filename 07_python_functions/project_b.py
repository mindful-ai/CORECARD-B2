# project b
# Program to get user input and
# extract all the prime numbers

'''
    input 12 13 14 15 16 16 17
    output [13, 17]
'''
import myprimes
print("project_b.py __name__ = ", __name__)
# input
n = input("Enter numbers separated by spaces: ")
n = n.split()
print(n)

# process
primes = []
for num in n:
    if(myprimes.checkprime(int(num)) == True):
        primes.append(int(num))

# output
print(primes)