# customEval.py
# Shaidullaev. N.


def comment(s):
    '''formats strings to create VPL comments'''
    print('Comment :=>> ' + s)


def grade(num):
    '''formats a number to create a VPL grade'''
    print('Grade :=>> ' + str(num))


points = 0
try:
    import square_function
except:
    comment("unable to import squareFunction")
    points += 0

try:
    square_function.square
except:
    comment("File submitted, but square() isn't defined")
    points += 0.5

try:
    if (type(square_function.square(4)) == int or type(square_function.square(4.0) == float)):
        comment("You did it! The function returns correct result and data type")
        points += 1
    else:
        comment("squareFunction.square doesn't return an int as required.")
        points -= -0.5
except:
    comment("squareFunction.square crashes")
    points += -0.5

grade(points)
