# customEval.py
# Shaidullaev. N.

import string
import random
import collections

def comment(s):
    '''formats strings to create VPL comments'''
    print('Comment :=>> ' + s)

def grade(num):
    '''formats a number to create a VPL grade'''
    print('Total Grade :=>> ' + str(num))

def test_buildCoder():
    points = 0          # variable to store the accumulated grade.
    
    # Test-1: Testing if file is exist and imported.
    try:
        import encryption
        comment("Test-1: The file was successfully loaded... ok\n +5 points")
        points += 5
    except:
        comment("Test-1: The file couldn't ne loaded. ERROR!")
        grade(points)
        exit()
        
    # Test-2: Testing if function buildCoder() is defined.
    try:
        encryption.buildCoder
        comment("Test-2: The function is defined... ok\n +5 points")
        points += 5
    except:
        comment("Test-2: The function is NOT defined.  ERROR")
        grade(points)
        exit()

    # Test-3: Testing the function buildCoder() with parameter 0.
    expected_output = {'A': 'A', 'C': 'C', 'B': 'B', 'E': 'E', 'D': 'D', 'G': 'G', 'F': 'F', 'I': 'I', 'H': 'H', 'K': 'K', 'J': 'J', 'M': 'M', 'L': 'L', 'O': 'O', 'N': 'N', 'Q': 'Q', 'P': 'P', 'S': 'S', 'R': 'R', 'U': 'U', 'T': 'T', 'W': 'W', 'V': 'V', 'Y': 'Y', 'X': 'X', 'Z': 'Z', 'a': 'a', 'c': 'c', 'b': 'b', 'e': 'e', 'd': 'd', 'g': 'g', 'f': 'f', 'i': 'i', 'h': 'h', 'k': 'k', 'j': 'j', 'm': 'm', 'l': 'l', 'o': 'o', 'n': 'n', 'q': 'q', 'p': 'p', 's': 's', 'r': 'r', 'u': 'u', 't': 't', 'w': 'w', 'v': 'v', 'y': 'y', 'x': 'x', 'z': 'z'}
    output = encryption.buildCoder(0)
    if expected_output == output:
        comment("Test-3: The buildCoder(0) returned the correct dictionary... ok\n +18 points")
        points += 18
    else:
        comment("Test-3: The buildCoder(0) returned INCORRECT output. ERROR!\nProgram output = " + str(output) + "\nExpected output = " + str(expected_output))
        
    # Test-4: Testing the function buildCoder() with parameter 22.
    expected_output = {'A': 'W', 'C': 'Y', 'B': 'X', 'E': 'A', 'D': 'Z', 'G': 'C', 'F': 'B', 'I': 'E', 'H': 'D', 'K': 'G', 'J': 'F', 'M': 'I', 'L': 'H', 'O': 'K', 'N': 'J', 'Q': 'M', 'P': 'L', 'S': 'O', 'R': 'N', 'U': 'Q', 'T': 'P', 'W': 'S', 'V': 'R', 'Y': 'U', 'X': 'T', 'Z': 'V', 'a': 'w', 'c': 'y', 'b': 'x', 'e': 'a', 'd': 'z', 'g': 'c', 'f': 'b', 'i': 'e', 'h': 'd', 'k': 'g', 'j': 'f', 'm': 'i', 'l': 'h', 'o': 'k', 'n': 'j', 'q': 'm', 'p': 'l', 's': 'o', 'r': 'n', 'u': 'q', 't': 'p', 'w': 's', 'v': 'r', 'y': 'u', 'x': 't', 'z': 'v'}
    output = encryption.buildCoder(22)
    if expected_output == output:
        comment("Test-4: The buildCoder(22) returned the correct dictionary... ok\n +18 points")
        points += 18
    else:
        comment("Test-4: The buildCoder(22) returned INCORRECT output. ERROR!\nProgram output = " + str(output) + "\nExpected output = " + str(expected_output))
        
    # Test-5: Testing the function buildCoder() with parameter 6.
    expected_output = {'A': 'G', 'C': 'I', 'B': 'H', 'E': 'K', 'D': 'J', 'G': 'M', 'F': 'L', 'I': 'O', 'H': 'N', 'K': 'Q', 'J': 'P', 'M': 'S', 'L': 'R', 'O': 'U', 'N': 'T', 'Q': 'W', 'P': 'V', 'S': 'Y', 'R': 'X', 'U': 'A', 'T': 'Z', 'W': 'C', 'V': 'B', 'Y': 'E', 'X': 'D', 'Z': 'F', 'a': 'g', 'c': 'i', 'b': 'h', 'e': 'k', 'd': 'j', 'g': 'm', 'f': 'l', 'i': 'o', 'h': 'n', 'k': 'q', 'j': 'p', 'm': 's', 'l': 'r', 'o': 'u', 'n': 't', 'q': 'w', 'p': 'v', 's': 'y', 'r': 'x', 'u': 'a', 't': 'z', 'w': 'c', 'v': 'b', 'y': 'e', 'x': 'd', 'z': 'f'}
    output = encryption.buildCoder(6)
    if expected_output == output:
        comment("Test-5: The buildCoder(6) returned the correct dictionary... ok\n +18 points")
        points += 18
    else:
        comment("Test-5: The buildCoder(6) returned INCORRECT output. ERROR!\nProgram output = " + str(output) + "\nExpected output = " + str(expected_output))

    # Test-6: Testing the function buildCoder() with parameter 14.
    expected_output = {'A': 'O', 'C': 'Q', 'B': 'P', 'E': 'S', 'D': 'R', 'G': 'U', 'F': 'T', 'I': 'W', 'H': 'V', 'K': 'Y', 'J': 'X', 'M': 'A', 'L': 'Z', 'O': 'C', 'N': 'B', 'Q': 'E', 'P': 'D', 'S': 'G', 'R': 'F', 'U': 'I', 'T': 'H', 'W': 'K', 'V': 'J', 'Y': 'M', 'X': 'L', 'Z': 'N', 'a': 'o', 'c': 'q', 'b': 'p', 'e': 's', 'd': 'r', 'g': 'u', 'f': 't', 'i': 'w', 'h': 'v', 'k': 'y', 'j': 'x', 'm': 'a', 'l': 'z', 'o': 'c', 'n': 'b', 'q': 'e', 'p': 'd', 's': 'g', 'r': 'f', 'u': 'i', 't': 'h', 'w': 'k', 'v': 'j', 'y': 'm', 'x': 'l', 'z': 'n'}
    output = encryption.buildCoder(14)
    if expected_output == output:
        comment("Test-6: The buildCoder(14) returned the correct dictionary... ok\n +18 points")
        points += 18
    else:
        comment("Test-6: The buildCoder(14) returned INCORRECT output. ERROR!\nProgram output = " + str(output) + "\nExpected output = " + str(expected_output))

    # Test-7: Testing the function buildCoder() with parameter 17.
    expected_output = {'A': 'R', 'C': 'T', 'B': 'S', 'E': 'V', 'D': 'U', 'G': 'X', 'F': 'W', 'I': 'Z', 'H': 'Y', 'K': 'B', 'J': 'A', 'M': 'D', 'L': 'C', 'O': 'F', 'N': 'E', 'Q': 'H', 'P': 'G', 'S': 'J', 'R': 'I', 'U': 'L', 'T': 'K', 'W': 'N', 'V': 'M', 'Y': 'P', 'X': 'O', 'Z': 'Q', 'a': 'r', 'c': 't', 'b': 's', 'e': 'v', 'd': 'u', 'g': 'x', 'f': 'w', 'i': 'z', 'h': 'y', 'k': 'b', 'j': 'a', 'm': 'd', 'l': 'c', 'o': 'f', 'n': 'e', 'q': 'h', 'p': 'g', 's': 'j', 'r': 'i', 'u': 'l', 't': 'k', 'w': 'n', 'v': 'm', 'y': 'p', 'x': 'o', 'z': 'q'}
    output = encryption.buildCoder(17)
    if expected_output == output:
        comment("Test-7: The buildCoder(17) returned the correct dictionary... ok\n +18 points")
        points += 18
    else:
        comment("Test-7: The buildCoder(17) returned INCORRECT output. ERROR!\nProgram output = " + str(output) + "\nExpected output = " + str(expected_output))

    # printing the total points accumulated.
    grade(points)


# run the test
test_buildCoder()
