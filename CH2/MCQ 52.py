def f(a):
  a = a + 1
  g(a)

def g(c):
  b = a + c
  h(b)

def h(a):
  print(a)

a = 5
f(3)