def faculteit(x):
    i = 1
    r = 1
    while i <= x:
        r = r+i
        i += 1
    return r

def binom(n, k):
    r = faculteit(n) / (faculteit(n-k) * faculteit(k))
    return r


p = binom (5, 2)
print (p)