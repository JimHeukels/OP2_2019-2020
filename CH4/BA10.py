def repeatStars(n):
  if n == 0:
    return ''
  else:
    half = repeatStars(n//2)
    if n % 2 == 0:
        extra = ''
    else:
        extra = '*'
    ret =  half  + extra +  half 
    return ret

n = 7
s = repeatStars(n)
print()