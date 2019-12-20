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

def triangle(x):
        s = ''
        while (x > 0):
                s = line(x) + '\n' + s
                x = x - 1
        return s         

ret = repeat(3, '#')
l = line(5)
t = triangle(6)
t2 = triangle(3)
print()