# 5! = 5 x 4 x 3 x 2 x 1 = 120

def factorial(n):
    x = [i for i in range(1, n+1)]
    prod = 1
    for i in x:
        prod = prod * i
    return prod

def fact(n):
    if n == 1:
        return 1
    else:
        return  n * fact(n-1)

if __name__ == "__main__":

    print(factorial(5))
    print(fact(5))