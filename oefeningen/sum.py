def sumFunction(x):
    xum = 0
    dum = 1
    while dum <= x:
        xum = xum + dum
        dum += 1
    return xum

#print(sumFunction((int(input('Nummertjen: ')))))

def recursiveAdd(total, count, filter):
    print('iteration')
    print(count)
    if count <= 0:
        return total
    else:
        total += count
        return recursiveAdd(total, count - 1)

print(recursiveAdd(0, 5))

while count <= 0:
    total += 1
    