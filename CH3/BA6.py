def repeat(n, sym):
    ret = ''
    while n > 0:

        ret = ret + str(sym)
        n = n - 1
        
    return ret

def line(x):
  return repeat(x, '*')  

def square(n):
  return repeat(n, line(n ) + '\n')

def rectangle(width, height):
  return repeat(height, line(width) + '\n')

s = square(5) 
r = rectangle(5, 3)
print()