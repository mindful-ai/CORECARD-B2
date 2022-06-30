# Program to determine if a number is prime or not

# input
n = int(input("Enter a number: "))

# Process/output

for i in range(2, n):
    if(n % i == 0):
        print("The number is not prime")
        break
else:
    print("The number is prime")

# loop else block can be written for both
# for loop and while loop

# IF the loop exits naturally, statements under
# loop else block executes once

# IF the loop exits because of break, the statements
# under loops else will not execute
