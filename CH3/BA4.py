def repeat(n, sym):
    ret = ''
    while n > 0:

        ret = ret + str(sym)
        n = n - 1
        
    return ret

n = 5
sym = '*'
ret = repeat(n, sym)
print()