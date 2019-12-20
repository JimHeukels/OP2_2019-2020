def line(n):
    if n <= 0:
        return ''
    return '*' + line(n - 1)

s = line(5)
print(s)