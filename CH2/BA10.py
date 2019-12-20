def ones(n):
  global s
  if n == 1:
    s = 'one'
  if n == 2:
    s = 'two'
  if n == 3:
    s = 'three'
  if n == 4:
    s = 'four'
  if n == 5:
    s = 'five'
  if n == 6:
    s = 'six'
  if n == 7:
    s = 'seven'
  if n == 8:
    s = 'eight'
  if n == 9:
    s = 'nine'

n = 9
s = ''
while n > 0:
  ones(n)
  n = n - 1
print()