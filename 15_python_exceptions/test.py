a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
res = 0
d = {'key':0}
try:
    res = a / b
except Exception as E:
    print("Cannot divide by zero", E)
else:
    print("RESULT  : ", res)
finally:
    print("Thank you!")

print('-----------------------------------------')

try:
    res = a / b
    print(d['key'])
    #f = open("abc.py")
    #x = 'f' + 10
except ZeroDivisionError:
    print("Cannot divide by zero")
except KeyError:
    print("Dont try to access keys which are not found")
except:
    print("Some other error")
else:
    print("RESULT  : ", res)
finally:
    print("Thank you!")