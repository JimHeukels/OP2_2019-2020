s = ''

def line(a, b):
    global s
    while a > 0:
        s = s + b
        a -= 1


line(5, '@')

def shape(m, c):
    global s
    iterator = 2     
    line(1, c) 
    s = s + '\n'
    while iterator <= m:
        line(iterator, c)
        iterator += 1
        s = s + "\n"
    #door de iterator van Samuel geeft de functie uiteindelijk wel het correcte antwoord, maar de stack frames kloppen niet met de verwachtte stackframes

s = ''
shape(4, '*')
print()