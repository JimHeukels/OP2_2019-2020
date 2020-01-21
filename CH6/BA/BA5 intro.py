hello = lambda x : 'Hello ' + str(x) + '!'

name = 'John'
a1 = hello(name)
a2 = (lambda s :  '<' + str(s) + '>'     )(hello ( name ))

v = 4
b = (lambda x : x * 2 )((lambda y : y + 1 )(v)) 

print()