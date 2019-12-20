def g(n):
  if n == 0:
    return ''
  partial = g(n//2)
  if n % 2 != 0:
    return partial + '1'
  return partial + '0'

def f(i,n,s):
  if i>=n:
    return ''
  seq = str(i) + ' : ' + g(i)
  ret = f(i + s, n, s)

f(1, 9, 3)
print(f)