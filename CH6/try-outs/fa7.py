def then(f, g):
  return lambda s : g(f(s))

def right(a, b, c):
  return lambda x : c(b(a(x)))

def left(a, b, c):
  return lambda x : a(b(c(x)))

def different(a, b):
  return lambda x : b(b(b(a(a(x))))) + '...stop'

one = lambda s : s + '1' 
two = lambda s : s + '2' 
three = lambda s : s + '3'  
four = lambda s : s + '4' 

res3 = different(one, two)('thirdtry')
print(res3)

res4 = right(one, two, left(four, two, different(three, four)))('challenge:')
print(res4)

right(one, two, left(four, two, different(three, four)))('challenge:')

#differen(three, four):
#  b(b(b(a(a(x))))) + '...stop'
#  b(b(b(a(a('...stop')))))
#  b(b(b(a())))
