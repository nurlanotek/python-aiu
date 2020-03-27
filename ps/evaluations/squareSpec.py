# customEval.py
# Shaidullaev. N.

def comment(s):
    '''formats strings to create VPL comments'''
    print('Comment :=>> ' + s)


def grade(num):
    '''formats a number to create a VPL grade'''
    print('Grade :=>> ' + str(num))

points = 0
# checking if squareFunction exist
try:
    import squareFunction
    comment("The squareFunction was successfully loaded... ok  +5 points")
    points += 5
except:
    comment("unable to import squareFunction. ERROR")
    points += 0
    exit()

try:
    squareFunction.square
    comment("File submitted, function square() is defined... ok +5 points")
    points += 5
except:
    comment("File submitted, but square() isn't defined... ERROR")
    exit()

try:
    if (type(squareFunction.square(4)) == int or type(squareFunction.square(4.0) == float)):
        comment("Returns correct data type... ok +10 points")
        points += 10
    else:
        comment("squareFunction.square doesn't return an int as required. ERROR")
        points -= 5
except:
    comment("squareFunction.square crashes. ERROR")
    points -= 5
    exit()
    
grade(points)
