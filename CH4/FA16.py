def f(n, m):
  if n > m:
    return 3
  elif n == m:
    return 7
  else:
    return 10 + f(n * 2, m)

res1 = f(2, 14) 
#res2 = f(4, 16)
#res3 = f(5, 233)
print(res1)