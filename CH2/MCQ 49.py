def f():
  a = a + 1
  g()

def g():
  print(a)

a = 5
f()