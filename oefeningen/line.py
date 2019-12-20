#We are trying to make a triangle shape by drawing lines of symbols. The symbol we are using is the asterisk ->  '*'
#Firstly we defined a function that would draw a line, according to the variable that is put into it.
#For instance, if we call the function 'line(5)' we would get the following pattern:
#   *****


def line(x):
    r = ""
    for i in range(x):
        r = r + '*'

    return r


#However, we are trying to draw a triangle, which, when the code has run sucesfully, should look like this:
#   *
#   **
#   ***
#   ****
#   *****

#the best way to do so, is by simply calling the line function multiple times, each with an incrementing variable for 'x'

def triangle(x):
    r = ""
    for i in range(x):
        line(x)
        r = r + '*'
        print (r)
    return r


(triangle(5))



