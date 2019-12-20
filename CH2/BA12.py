seq = ''
arg = 10
def zero2N(n):
    global seq
    i = 0
    while i < n:
        number = str(i)
        seq = seq + number + ' '
        i = i + 1
    
    

zero2N(arg)
print()