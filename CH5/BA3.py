def rseq (a, b):
  print()
  if a == b:
    return a
  if b < a:
    return ''
  else:
    part = rseq(a+1, b-1)
    ans = str(a) + str(part) + str(b)
    return ans

a = 1
b = 9 
ans = rseq(a, b)
print()