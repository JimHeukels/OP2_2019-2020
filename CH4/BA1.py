def sumUpTo(n):
  if n <= 0:
    return 0  
  else:
    temp = sumUpTo(n-1)  
    return temp + n

a = 5
result = sumUpTo(a)
print()