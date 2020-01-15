def line(n):
  if n == 0:
    return ''
  else:
    s = '*'
    res = s + line(n-1)
    return res

def rectangle2(rows, cols):
  if rows == 0:
    return ''  
  else:
    half = rows // 2
    halfRectangle = rectangle2(half, cols)  
    if rows % 2 != 0:
      add = line(cols) + '\n'
    else:
      add = ''
      
    return halfRectangle + add + halfRectangle 

rect = rectangle2(3, 4)
print