def difference (input1, input2):
    return lambda x : input1(x) - input2(x)


half = lambda  x : x // 2 
squared = lambda  x : x ** 2 
f1 = half
f2 = squared
f = difference(f1, f2)
x = 10
ans = f(x)
print()