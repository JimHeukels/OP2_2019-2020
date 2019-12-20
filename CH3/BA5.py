def repeat(n, sym):
    ret = ''
    while n > 0:

        ret = ret + str(sym)
        n = n - 1
        
    return ret

def line(x  ):
  return repeat(x, '*')  

outcome = line(5)
outcome = line(10)
print()