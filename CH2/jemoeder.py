def table(a, b):
    global final
    final = ''
    while b > 0:
        calc = a * b
        final = str(b) + ' x ' + str(a) + ' = ' + str(calc) + '\n' + final
        b -= 1
    return final
table(4, 5)
table(3, 10)
print(final) 