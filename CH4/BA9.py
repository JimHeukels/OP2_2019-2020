def repeat(n, sym):
  if n <= 0 :
    return ''  
  else:
    partial = repeat(n-1, sym)  
    res = sym + partial  
    return res

n = 5
sym = '#'
s = repeat(n, sym)
print()