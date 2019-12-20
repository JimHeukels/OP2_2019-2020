def count(a, b):
  if a > b:
    return ''
  else:
    partial = count(a+1, b) 
    ret = str(a) + partial
    return ret

a = 4
b = 8
s = count(a, b)
print()