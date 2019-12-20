def rangeSum(l, u):
  if l > u  :
    return  0 
  elif l == u:
    return l  
  else: 
    partial = rangeSum(l + 1, u - 1)
    res =  l  + partial +  u 
    return res

l = 6
u = 11
sum = rangeSum(l, u)
print()