# ---- THANKS LENNARD ----

def isDivisible(a, b):
        if a % b == 0:
                return True
        else:
                return False

def isLeap(a):
        return a % 4 == 0 and (a % 100 != 0 or a % 400 == 0)

param = 2019

test = isDivisible(param, 4)
test = isLeap(param)
print()