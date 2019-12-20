def prodUpTo(n):
  if n <= 1  :
    return 1  
  else:
    temp = prodUpTo(n-1)  
    return temp * n

a = 5
result = prodUpTo(a)
print()