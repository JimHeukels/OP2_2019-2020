def myrange(x, y, z):
    global seq
    if (x < y):
        while (x < y):
            if z == 0:
                seq = 'Error: step size cannot be zero'
                break
            seq = seq + str(x)
            x = x + z
    
    elif (y < x):
        while (y < x):
            if z == 0:
                seq = 'Error: step size cannot be zero'
                break
            seq = seq + str(x)
            x = x + z

seq = ''
start = 1
end = 10
step = 1
myrange(start, end, step)
print()