def repeat(n, sym):
  if n == 0:
    return ''
  else:
    rest = sym + repeat (n-1, sym)
    return rest

def line(n):
  return repeat(n, '*')  

def spaces(n):
  return repeat(n, ' ')  

def trapezoid(l, u):
  if(l > u):
    return ''  
  else:
    oneLine = line(l)   + '\n'
    partial = trapezoid(l + 2, u) 
    n = (u - l) // 2 
    sp = spaces (n)
    return sp + oneLine + partial

l = 3
u = 9
t = trapezoid(l, u)
print()