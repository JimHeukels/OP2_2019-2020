def rseq(a, b, i):
  print()
  if a > b:
    return ''
  else:
    number = rseq(a+i, b, i)
    res = str(a) + str(number)
    return res

a = 1
b = 7
i = 2
s = rseq(a, b, i)
print()