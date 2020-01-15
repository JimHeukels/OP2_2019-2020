incr = lambda x : x + 1
dec = lambda x : x - 1
iseven = lambda x : x % 2 == 0
dub = lambda x : x + x



then = lambda f,g: lambda x : f(g(x))

myfunc = then(incr, dub)

v = myfunc(5)
print(v)

#incr>dub>dec>dub

v = thisFunc(5)
print(v)



