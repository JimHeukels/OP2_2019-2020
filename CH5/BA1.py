def rsum(n):
  print()

  if n <= 0:
    return 0

  else:
    number = rsum(n-1)
    res = number + n
    return res

n = 5
s = rsum(n)
print()