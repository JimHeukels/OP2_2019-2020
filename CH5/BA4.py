def f(n, s):
  print()
  
  if n == 0:
    return ''
    
  else:
    
    s = str(n) + ' '
    s = f(n-1, s) + str(n) + ' '
    return s

res = f(10, '')
print()