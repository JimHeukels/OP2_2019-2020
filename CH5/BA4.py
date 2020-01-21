def f(n, s):
  print()
  if n < 1:

    return s
  
  else:

    return f(n-1, str(n) + ' ' + s)

res = f(10, '')
print()