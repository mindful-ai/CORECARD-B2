# Write a program to determine if the result was positive, negative or zero
# after subtracting two numbers

# input
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# a = int(a)

# process
res = a - b

# output
print("DIFFERENCE: ", abs(a - b))
if (res > 0):
    print("The result is positive")
elif (res < 0):
    print("The result is negative")
else:
    print("The result is zero")
    
