def f(n):
  if n < 0: 
    n = -n 
  if n == 0:
    return 0
  else:
    return n % 10 + f(n // 10)

s1 = f(1348)
s2 = f(-352)

print(s1)
print(s2)