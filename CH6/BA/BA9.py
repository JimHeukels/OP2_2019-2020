def OR (inputX, inputY):
  return lambda x : inputX(x) or inputY(x)

def AND (inputA, inputB):
  return lambda x : inputA(x) and inputB(x) 

def CONCAT(f, g): 
  return  lambda x : f(x) + g(x) 

f1 =  lambda x : x % 2 != 0
f2 =  lambda x : x > 0 
surround =  lambda x : '[' + str(x) + ']' 
toStar =  lambda x : '*' 

a = -7
b = 9
c = 5
res1 = OR(f1, f2)(a)
res1b = AND(f1, f2)(a)
res2 = OR(f1, f2)(b)
res2b = AND(f1, f2)(b)
res3 = CONCAT(surround, toStar)(c)
res4 = CONCAT(toStar, surround)(c)
print()