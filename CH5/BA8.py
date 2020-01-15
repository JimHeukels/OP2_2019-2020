def line(n):
  if n == 0:
    return ''
  else:
    rest = line(n-1)
    return rest + '*'

def rectTrapezoid(l, u):
  if l > u:
    return ''
  else:
    oneLine = line(l)
    partial = rectTrapezoid(l+1, u) 
    return oneLine + '\n' + partial 

l = 3
u = 6
rt = rectTrapezoid(l, u)
print()