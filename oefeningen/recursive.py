# --- Non-recursieve versie ---
def som(n):
    s = 0
    while n > 0:
        s = s + n
        n = n - 1
    return s


# --- Recursieve versie ---
def somR(n):
    if n > 0:
        s = n + somR(n - 1)
    else:
        s = 0
    return s

r = somR(3)
#print(r)

f = som(5)
ff = somR(5)
#print(f, ff)


# --- Non-recursieve faculteit
def fac(n):
    s = 1
    while n > 0:
        s = s * n
        n = n - 1
    return s


# --- Recursieve faculteit ---
def facR(n):
    if n > 1:
        s = n * facR(n - 1)
    else:
        s = 1
    return s

rr = facR(5)
#print(rr)


# --- Recursieve sterretjens
def sterR(n):
    sym = '*'
    s = ''
    if n > 0:
        s = sym + str(sterR(n - 1))
    return s

zz = sterR(5)
#print (zz)


# --- Recursieve pyramide
def pyrR(n):
    if n <= 0:
        return sterR(0)
    else:
        return sterR(n) + '\n' + pyrR(n-1)

zzz = pyrR(3)
print(zzz)