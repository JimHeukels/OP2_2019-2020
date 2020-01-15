f = lambda a, b  : (a + b) ** 2
g = lambda a, b :  a ** 2  +  b ** 2 + 2 * a * b

eq = lambda x, y : x  == y 

l = f(2 , 3)
r = g(3, 4)

res = eq(l, r)
res = eq( f(1, 2), g(2, 1) )
print()