# ---- THANKS LENNARD ----

def isPrime(number):
    x = True
    y = 2
    while number > y:
        if number % y == 0:
            x = False
        y += 1
    return x

def primeSequence(number):
    x = ''
    y = 1
    while number >= y:
        y += 1
        n = isPrime(y)
        if n == True:
            x += str(y) + ', '
        if number == y:
            return x

input = 13
x = isPrime(input)
x = primeSequence(input)
print()