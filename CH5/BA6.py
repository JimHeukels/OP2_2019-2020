def line(n):
  if n == 0:
    return ''
  else:
    rest = line(n-1)
    return rest + '*'

def rectangle(amountRows, amountColumns):
  if amountRows == 0:
    return ''
  else:
    partial = rectangle(amountRows-1, amountColumns)  
    singleLine = line(amountColumns) + '\n'
    return singleLine + partial

rect = rectangle(3, 5)
print()