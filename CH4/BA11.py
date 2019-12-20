def repeat(n, sym): 
  if n <= 0:
    return '' 
  else: 
    part = repeat(n//2, sym)  
    res = sym * n
    return res

n = 5
sym = '*'
s = repeat(5, sym)
print(s)