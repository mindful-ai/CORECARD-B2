# project a
# new approach using a function definition


# Function definition
def checkprime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

def getprimes(start, end):
    pass

def gethighestprime(n):
    pass

print("myprimes.py __name__ = ", __name__)

if __name__ == '__main__':
    # input
    n = int(input("Enter a number: "))

    # process/output
    if(checkprime(n) == True):
        print('The number is prime')
    else:
        print('The number is not prime')


# -------------------------------------

'''

>python
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import myprimes
Enter a number: 13
The number is prime
>>> myprimes.checkprime(12)
False
>>> myprimes.checkprime(13)
True
>>>

'''

# -------------------------------------