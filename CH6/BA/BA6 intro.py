f1 = lambda x : x * 2 
f2 = lambda x : x + 1  
f3 = lambda s : str(s) + '*'  
f4 = lambda a , b : '<' + str(a) + ' - ' + str(b) + '>'  
f5 = lambda s1 , s2 : str(s2) + ' --> ' + str(s1) 

v = 5
s = 'bim'
a = f1(v)
b = f2(v)
c = f3(s)
v2 = 7
s2 = 'bam'
d = f4(v, v2)
e = f5(s, s2)
print()