# --- FIXED IT BROOO --- 

def line(a, b):
    global s
    while a > 0:
        s = s + b
        a -= 1
    
s = ''
line(5, '@')

def shape(m, c):
    global s
    i = 1
    while i <= m: 
        line(i, c)  
        i = i + 1
        s = s + '\n'

s = ''
shape(4, '*')
print()