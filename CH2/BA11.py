def ones(n):
  global s
  if n == 1:
    s = s + 'one'
  if n == 2:
    s = s + 'two'
  if n == 3:
    s = s + 'three'
  if n == 4:
    s = s + 'four'
  if n == 5:
    s = s + 'five'
  if n == 6:
    s = s + 'six'
  if n == 7:
    s = s + 'seven'
  if n == 8:
    s = s + 'eight'
  if n == 9:
    s = s + 'nine'

    
def tens(n):
  global s, i
  if n == 1:
    s = 'ten'
  if n == 2:
    s = 'twenty'
  if n == 3:
    s = 'thirty'
  if n == 4:
    s = 'forty'
  if n == 5:
    s = 'fifty'
  if n == 6:
    s = 'sixty'
  if n == 7:
    s = 'seventy'
  if n == 8:
    s = 'eighty'
  if n == 9:
    s = 'ninety'


def inwords(p):
  global s
  if p >= 20 and p < 100:
    if p // 10 > 1: 
      tens(p // 10 )
    if p % 10 > 0: 
      s = s + ' '
      ones(p % 10 )

step = 7
i = 20 
while i < 100:
    s = ''
    inwords(i)
    i = i + step 