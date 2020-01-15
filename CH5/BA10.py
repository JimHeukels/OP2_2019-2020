def lineHoles(i, n, sym, times):
  if i == n:
    return ''
  else:
    rest = lineHoles(i+1, n, sym, times)  
    if i % multipleOf == 0:
      rest = str(i) + rest
      return rest
    else:
      rest = str(sym) + rest
      return rest

n = 7
sym = '+'
multipleOf = 3
s = lineHoles(0, n, sym, multipleOf)
print(s)