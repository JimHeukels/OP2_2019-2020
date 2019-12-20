def count(a, b):
  if a > b:
    return ''
  else:
    partial = count(a, b-1)
    ret = partial + str(b)  
    return ret

a = 2
b = 5
s = count(a, b)
print()