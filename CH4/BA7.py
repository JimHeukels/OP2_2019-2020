def count(a, b):
  if a > b:
    return ''
  elif a == b:
    return str(a)
  else:
    partial = count(a+1, b-1)
    ret = str(a) + partial + str(b)
    return ret

a = 0
b = 6
s = count(a, b)
print()