incr = lambda x : x + 1
isEven = lambda x : x % 2 == 0
dub = lambda x : x + x

def then(f, g):
    return lambda x: f(f(g(x)))

def isEvenAfterIncr(x):
    return isEven(incr(x))


v = isEvenAfterIncr(5)
print (v)


myIsEvenAfterIncr = then(isEven, incr)
myIncrAndDouble = then(incr, dub)

v = myIsEvenAfterIncr(5)
print (v)

v = myIncrAndDouble(5)
print (v)

myFunc = then(incr, dub)

