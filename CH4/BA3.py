def numsToString(n):
  if n <= 0:
    return ''
  else:
    temp = numsToString(n-1)  
    s = temp + str(n) + ' '
    return s

a = 5
res = numsToString(a)
print()