def sqr(x):
    z = x * x
    return z

def sumOfSqr(x):
    y = 0
    while x > 0:
        y = y + sqr(x)
        x = x - 1
    return y

a = sqr(5)
a = sumOfSqr(5)
a = sumOfSqr( sqr(2) )
print()