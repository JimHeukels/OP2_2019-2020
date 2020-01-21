div2 =  lambda x : x // 2  
isEven =  lambda x : x % 2 == 0 
isOdd =  lambda x: x % 2 != 0 
greaterThan =  lambda x, y : x > y 

v = 5
a = div2(v)
b = isEven(v)
c = isOdd(v)
d = greaterThan(v, 2)
e = greaterThan(v, 7)
print()