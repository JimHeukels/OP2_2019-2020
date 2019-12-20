def log(n, base):
  if n < base:
    return 0
  else:
    return 1 + log(n // base, base)

#v1 = log(8, 2) 
#v2 = log(16, 4)
v3 = log(243, 3)
print(v3)