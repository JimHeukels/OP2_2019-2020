def repeatStar(n):
  if n <= 0:
    return ''  
  else:
    temp = repeatStar(n-1)  
    s = '*'   + temp  
    return s

a = 4
res = repeatStar(a)
print()