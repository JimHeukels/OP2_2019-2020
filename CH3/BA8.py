def repeat(x, sym):
  s = ''
  while (x > 0):
    s = s + str(sym)
    x = x - 1
  return s

def line(x):
  s = ''
  while (x > 0):
    s = s + '*'
    x = x - 1
  return s

def hollowLine(n):
  l = n - 2
  spaces = repeat(n, ' '  )
  s = '*' + spaces + '*'
  return s

def hollowSquare(n):
  l = line(n  )
  hl = hollowLine(n-2  )
  r = repeat(n-2, hl + '\n')
  s = l + '\n' + r + l + '\n' 
  return s

s = hollowSquare(5)
s = hollowSquare(4)
print()