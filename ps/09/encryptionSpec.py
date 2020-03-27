# customEval.py
# Shaidullaev. N.

import string
import random


def comment(s):
    '''
    Formats strings to create VPL comments.
    '''
    print(s)


def grade(num):
    """
    Formats a number to create a VPL grade
    """
    print(' + ------------------------')
    print('\t\t\tTotal Grade = ' + str(num))


def test_build_coder():
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
        
    # Test-2: Testing if function build_coder() is defined.
    try:
        assert encryption.build_coder
        comment("Test-2: The function is defined... ok\n +5 points")
        points += 5
    except:
        comment("Test-2: The function is NOT defined.  ERROR")
        grade(points)
        exit()

    # Test-3: Testing the function build_coder() with parameter 0.
    expected_output = {'A': 'A', 'C': 'C', 'B': 'B', 'E': 'E', 'D': 'D', 'G': 'G', 'F': 'F', 'I': 'I', 'H': 'H', 'K': 'K', 'J': 'J', 'M': 'M', 'L': 'L', 'O': 'O', 'N': 'N', 'Q': 'Q', 'P': 'P', 'S': 'S', 'R': 'R', 'U': 'U', 'T': 'T', 'W': 'W', 'V': 'V', 'Y': 'Y', 'X': 'X', 'Z': 'Z', 'a': 'a', 'c': 'c', 'b': 'b', 'e': 'e', 'd': 'd', 'g': 'g', 'f': 'f', 'i': 'i', 'h': 'h', 'k': 'k', 'j': 'j', 'm': 'm', 'l': 'l', 'o': 'o', 'n': 'n', 'q': 'q', 'p': 'p', 's': 's', 'r': 'r', 'u': 'u', 't': 't', 'w': 'w', 'v': 'v', 'y': 'y', 'x': 'x', 'z': 'z'}
    output = encryption.build_coder(0)
    if expected_output == output:
        comment("Test-3: The buildCoder(0) returned the correct dictionary... ok\n +18 points")
        points += 18
    else:
        comment("Test-3: The buildCoder(0) returned INCORRECT output. ERROR!\nProgram output = " + str(output) + "\nExpected output = " + str(expected_output))
        exit()
        
    # Test-4: Testing the function buildCoder() with parameter 22.
    expected_output = {'A': 'W', 'C': 'Y', 'B': 'X', 'E': 'A', 'D': 'Z', 'G': 'C', 'F': 'B', 'I': 'E', 'H': 'D', 'K': 'G', 'J': 'F', 'M': 'I', 'L': 'H', 'O': 'K', 'N': 'J', 'Q': 'M', 'P': 'L', 'S': 'O', 'R': 'N', 'U': 'Q', 'T': 'P', 'W': 'S', 'V': 'R', 'Y': 'U', 'X': 'T', 'Z': 'V', 'a': 'w', 'c': 'y', 'b': 'x', 'e': 'a', 'd': 'z', 'g': 'c', 'f': 'b', 'i': 'e', 'h': 'd', 'k': 'g', 'j': 'f', 'm': 'i', 'l': 'h', 'o': 'k', 'n': 'j', 'q': 'm', 'p': 'l', 's': 'o', 'r': 'n', 'u': 'q', 't': 'p', 'w': 's', 'v': 'r', 'y': 'u', 'x': 't', 'z': 'v'}
    output = encryption.build_coder(22)
    if expected_output == output:
        comment("Test-4: The buildCoder(22) returned the correct dictionary... ok\n +18 points")
        points += 18
    else:
        comment("Test-4: The buildCoder(22) returned INCORRECT output. ERROR!\nProgram output = " + str(output) + "\nExpected output = " + str(expected_output))
        exit()
        
    # Test-5: Testing the function buildCoder() with parameter 6.
    expected_output = {'A': 'G', 'C': 'I', 'B': 'H', 'E': 'K', 'D': 'J', 'G': 'M', 'F': 'L', 'I': 'O', 'H': 'N', 'K': 'Q', 'J': 'P', 'M': 'S', 'L': 'R', 'O': 'U', 'N': 'T', 'Q': 'W', 'P': 'V', 'S': 'Y', 'R': 'X', 'U': 'A', 'T': 'Z', 'W': 'C', 'V': 'B', 'Y': 'E', 'X': 'D', 'Z': 'F', 'a': 'g', 'c': 'i', 'b': 'h', 'e': 'k', 'd': 'j', 'g': 'm', 'f': 'l', 'i': 'o', 'h': 'n', 'k': 'q', 'j': 'p', 'm': 's', 'l': 'r', 'o': 'u', 'n': 't', 'q': 'w', 'p': 'v', 's': 'y', 'r': 'x', 'u': 'a', 't': 'z', 'w': 'c', 'v': 'b', 'y': 'e', 'x': 'd', 'z': 'f'}
    output = encryption.build_coder(6)
    if expected_output == output:
        comment("Test-5: The buildCoder(6) returned the correct dictionary... ok\n +18 points")
        points += 18
    else:
        comment("Test-5: The buildCoder(6) returned INCORRECT output. ERROR!\nProgram output = " + str(output) + "\nExpected output = " + str(expected_output))
        exit()

    # Test-6: Testing the function buildCoder() with parameter 14.
    expected_output = {'A': 'O', 'C': 'Q', 'B': 'P', 'E': 'S', 'D': 'R', 'G': 'U', 'F': 'T', 'I': 'W', 'H': 'V', 'K': 'Y', 'J': 'X', 'M': 'A', 'L': 'Z', 'O': 'C', 'N': 'B', 'Q': 'E', 'P': 'D', 'S': 'G', 'R': 'F', 'U': 'I', 'T': 'H', 'W': 'K', 'V': 'J', 'Y': 'M', 'X': 'L', 'Z': 'N', 'a': 'o', 'c': 'q', 'b': 'p', 'e': 's', 'd': 'r', 'g': 'u', 'f': 't', 'i': 'w', 'h': 'v', 'k': 'y', 'j': 'x', 'm': 'a', 'l': 'z', 'o': 'c', 'n': 'b', 'q': 'e', 'p': 'd', 's': 'g', 'r': 'f', 'u': 'i', 't': 'h', 'w': 'k', 'v': 'j', 'y': 'm', 'x': 'l', 'z': 'n'}
    output = encryption.build_coder(14)
    if expected_output == output:
        comment("Test-6: The buildCoder(14) returned the correct dictionary... ok\n +18 points")
        points += 18
    else:
        comment("Test-6: The buildCoder(14) returned INCORRECT output. ERROR!\nProgram output = " + str(output) + "\nExpected output = " + str(expected_output))
        exit()

    # Test-7: Testing the function buildCoder() with parameter 17.
    expected_output = {'A': 'R', 'C': 'T', 'B': 'S', 'E': 'V', 'D': 'U', 'G': 'X', 'F': 'W', 'I': 'Z', 'H': 'Y', 'K': 'B', 'J': 'A', 'M': 'D', 'L': 'C', 'O': 'F', 'N': 'E', 'Q': 'H', 'P': 'G', 'S': 'J', 'R': 'I', 'U': 'L', 'T': 'K', 'W': 'N', 'V': 'M', 'Y': 'P', 'X': 'O', 'Z': 'Q', 'a': 'r', 'c': 't', 'b': 's', 'e': 'v', 'd': 'u', 'g': 'x', 'f': 'w', 'i': 'z', 'h': 'y', 'k': 'b', 'j': 'a', 'm': 'd', 'l': 'c', 'o': 'f', 'n': 'e', 'q': 'h', 'p': 'g', 's': 'j', 'r': 'i', 'u': 'l', 't': 'k', 'w': 'n', 'v': 'm', 'y': 'p', 'x': 'o', 'z': 'q'}
    output = encryption.build_coder(17)
    if expected_output == output:
        comment("Test-7: The buildCoder(17) returned the correct dictionary... ok\n +18 points")
        points += 18
    else:
        comment("Test-7: The buildCoder(17) returned INCORRECT output. ERROR!\nProgram output = " + str(output) + "\nExpected output = " + str(expected_output))
        exit()

    # printing the total points accumulated.
    grade(points)
# run the test for buildCoder()
# test_build_coder()


def test_apply_coder():
    points = 0  # variable to store the accumulated grade.

    # Prerequisite-1: Testing if file is exist and imported.
    try:
        import encryption
        comment("Prerequisite-1: The file was successfully loaded... ok")
    except:
        comment("Prerequisite-1: The file couldn't ne loaded. ERROR!")
        grade(points)
        exit()

    # Prerequisite-2: Testing if function buildCoder() is defined.
    try:
        encryption.apply_coder
        comment("Prerequisite-2: The function is defined... ok")
    except:
        comment("Prerequisite-2: The function apply_coder() is NOT defined.  ERROR")
        grade(points)
        exit()

    # Test-1: Testing the function apply_coder().
    output = encryption.apply_coder('Hello, world!', encryption.build_coder(0))
    expected_output = 'Hello, world!'
    if expected_output == output:
        comment("Test-1: The Function returned the correct value... ok\n +10 points")
        points += 10
    else:
        comment("Test-1: The function returned INCORRECT value. ERROR!\nFunction returned = " + str(output) + "\nExpected output = " + str(expected_output))
        exit()

    # Test-2: Testing the function apply_coder().
    output = encryption.apply_coder('Hello, world!', encryption.build_coder(12))
    expected_output = 'Tqxxa, iadxp!'
    if expected_output == output:
        comment("Test-2: The Function returned the correct value... ok\n +10 points")
        points += 10
    else:
        comment("Test-2: The function returned INCORRECT value. ERROR!\nFunction returned = " + str(
            output) + "\nExpected output = " + str(expected_output))
        exit()

    # Test-3: Testing the function apply_coder().
    output = encryption.apply_coder('Hello, world!', encryption.build_coder(1))
    expected_output = 'Ifmmp, xpsme!'
    if expected_output == output:
        comment("Test-3: The Function returned the correct value... ok\n +10 points")
        points += 10
    else:
        comment("Test-3: The function returned INCORRECT value. ERROR!\nFunction returned = " + str(
            output) + "\nExpected output = " + str(expected_output))
        exit()

    # Test-4: Testing the function apply_coder().
    output = encryption.apply_coder('Hello, world!', encryption.build_coder(23))
    expected_output = 'Ebiil, tloia!'
    if expected_output == output:
        comment("Test-4: The Function returned the correct value... ok\n +10 points")
        points += 10
    else:
        comment("Test-4: The function returned INCORRECT value. ERROR!\nFunction returned = " + str(
            output) + "\nExpected output = " + str(expected_output))
        exit()

    # Test-5: Testing the function apply_coder().
    output = encryption.apply_coder('The quiz is... hard!', encryption.build_coder(0))
    expected_output = 'The quiz is... hard!'
    if expected_output == output:
        comment("Test-5: The Function returned the correct value... ok\n +10 points")
        points += 10
    else:
        comment("Test-5: The function returned INCORRECT value. ERROR!\nFunction returned = " + str(
            output) + "\nExpected output = " + str(expected_output))
        exit()

    # Test-6: Testing the function apply_coder().
    output = encryption.apply_coder('The quiz is... hard!', encryption.build_coder(12))
    expected_output = 'Ftq cgul ue... tmdp!'
    if expected_output == output:
        comment("Test-6: The Function returned the correct value... ok\n +10 points")
        points += 10
    else:
        comment("Test-6: The function returned INCORRECT value. ERROR!\nFunction returned = " + str(
            output) + "\nExpected output = " + str(expected_output))
        exit()

    # Test-7: Testing the function apply_coder().
    output = encryption.apply_coder('The quiz is... hard!', encryption.build_coder(1))
    expected_output = 'Uif rvja jt... ibse!'
    if expected_output == output:
        comment("Test-7: The Function returned the correct value... ok\n +10 points")
        points += 10
    else:
        comment("Test-7: The function returned INCORRECT value. ERROR!\nFunction returned = " + str(
            output) + "\nExpected output = " + str(expected_output))
        exit()

    # Test-8: Testing the function apply_coder().
    output = encryption.apply_coder('The quiz is... hard!', encryption.build_coder(23))
    expected_output = 'Qeb nrfw fp... exoa!'
    if expected_output == output:
        comment("Test-8: The Function returned the correct value... ok\n +10 points")
        points += 10
    else:
        comment("Test-8: The function returned INCORRECT value. ERROR!\nFunction returned = " + str(
            output) + "\nExpected output = " + str(expected_output))
        exit()

    # Test-9: Testing the function apply_coder().
    output = encryption.apply_coder('12 jackdaws quizzed my sphinx!?', encryption.build_coder(0))
    expected_output = '12 jackdaws quizzed my sphinx!?'
    if expected_output == output:
        comment("Test-9: The Function returned the correct value... ok\n +10 points")
        points += 10
    else:
        comment("Test-9: The function returned INCORRECT value. ERROR!\nFunction returned = " + str(
            output) + "\nExpected output = " + str(expected_output))
        exit()

    # Test-10: Testing the function apply_coder().
    output = encryption.apply_coder('12 jackdaws quizzed my sphinx!?', encryption.build_coder(12))
    expected_output = '12 vmowpmie cgullqp yk ebtuzj!?'
    if expected_output == output:
        comment("Test-10: The Function returned the correct value... ok\n +10 points")
        points += 10
    else:
        comment("Test-10: The function returned INCORRECT value. ERROR!\nFunction returned = " + str(
            output) + "\nExpected output = " + str(expected_output))
        exit()

    # printing the total grade
    grade(points)
# run the test for applyCoder()
# test_apply_coder()


def test_apply_shift():
    points = 0  # variable to store the accumulated grade.

    # Prerequisite-1: Testing if file is exist and imported.
    try:
        import encryption
        comment("Prerequisite-1: The file was successfully loaded... ok")
    except:
        comment("Prerequisite-1: The file couldn't ne loaded. ERROR!")
        grade(points)
        exit()

    # Prerequisite-2: Testing if function buildCoder() is defined.
    try:
        encryption.apply_shift
        comment("Prerequisite-2: The function apply_shift() is defined... ok")
    except:
        comment("Prerequisite-2: The function apply_shift() is NOT defined.  ERROR")
        grade(points)
        exit()

    # Test-1: Testing the function apply_coder().
    output = encryption.apply_shift('Hello, world!', 15)
    expected_output = 'Wtaad, ldgas!'
    if expected_output == output:
        comment("Test-1: The Function returned the correct value... ok\n +20 points")
        points += 20
    else:
        comment("Test-1: The function returned INCORRECT value. ERROR!\n\nFunction returned = " + str(
            output) + "\nExpected output = " + str(expected_output) + "\n")
        exit()

    # Test-2: Testing the function apply_coder().
    output = encryption.apply_shift('The quiz is... hard!', 1)
    expected_output = 'Uif rvja jt... ibse!'
    if expected_output == output:
        comment("Test-2: The Function returned the correct value... ok\n +20 points")
        points += 20
    else:
        comment("Test-2: The function returned INCORRECT value. ERROR!\nFunction returned = " + str(
            output) + "\nExpected output = " + str(expected_output))
        exit()

    # Test-3: Testing the function apply_coder().
    output = encryption.apply_shift('12 jackdaws quizzed my sphinx!?', 10)
    expected_output = '12 tkmunkgc aesjjon wi czrsxh!?'
    if expected_output == output:
        comment("Test-3: The Function returned the correct value... ok\n +20 points")
        points += 20
    else:
        comment("Test-3: The function returned INCORRECT value. ERROR!\nFunction returned = " + str(
            output) + "\nExpected output = " + str(expected_output))
        exit()

    # Test-4: Testing the function apply_coder().
    output = encryption.apply_shift('rlghu', 0)
    expected_output = 'rlghu'
    if expected_output == output:
        comment("Test-4: The Function returned the correct value... ok\n +20 points")
        points += 20
    else:
        comment("Test-4: The function returned INCORRECT value. ERROR!\nFunction returned = " + str(
            output) + "\nExpected output = " + str(expected_output))
        exit()

    # Test-5: Testing the function apply_coder().
    output = encryption.apply_shift('amrntqjypwhxgd', 6)
    expected_output = 'gsxtzwpevcndmj'
    if expected_output == output:
        comment("Test-5: The Function returned the correct value... ok\n +20 points")
        points += 20
    else:
        comment("Test-5: The function returned INCORRECT value. ERROR!\nFunction returned = " + str(
            output) + "\nExpected output = " + str(expected_output))
        exit()


    # printing the total grade
    print('----------------------------')
    grade(points)
# run the test fir apply_shift()
# test_apply_shift()

def test_find_best_shift():
    points = 0  # variable to store the accumulated grade.
    # Prerequisite-1: Testing if file is exist and imported.
    try:
        import encryption
        comment("Prerequisite-1: The file was successfully loaded ...\t\tok\n")
    except:
        comment("Prerequisite-1: The file couldn't ne loaded. ERROR!\n")
        grade(points)
        exit()
    else:
        wordList = encryption.loadWords()
        print()

    # Prerequisite-2: Testing if function buildCoder() is defined.
    try:
        encryption.find_best_shift
        comment("Prerequisite-2: The function apply_shift() is defined ...\tok\t\n")
    except:
        comment("Prerequisite-2: The function apply_shift() is NOT defined.  ERROR\n")
        grade(points)
        exit()

    # Test-1: Testing the function apply_coder().
    output = encryption.find_best_shift(wordList, 'MJQqt, btwqi!')
    expected_output = 21
    if expected_output == output:
        comment("Test-1: The Function returned the correct value ...\t\tPassed\t(+10 points)")
        points += 10
    else:
        comment("Test-1: Failed - The function returned INCORRECT value. ERROR!\n\nFunction returned = " + str(
            output) + "\nbut\nExpected output = " + str(expected_output) + "\n")
        exit()

    # Test-2: Testing the function apply_coder().
    output = encryption.find_best_shift(wordList, 'XlI uymd mw... levh!')
    expected_output = 22
    if expected_output == output:
        comment("Test-2: The Function returned the correct value ...\t\tPassed\t(+10 points)")
        points += 10
    else:
        comment("Test-2: The Function returned INCORRECT value ... \t\tFAILED\n\nFunction returned = " + str(
            output) + "\nbut\nExpected output is = " + str(expected_output) + "\n")
        exit()

    # Test-3: Testing the function apply_coder().
    output = encryption.find_best_shift(wordList, "DRo Dokmrob'C xkWo sc DKlSdRk?")
    expected_output = 16
    if expected_output == output:
        comment("Test-3: The Function returned the correct value ...\t\tPassed\t(+10 points)")
        points += 10
    else:
        comment("Test-3: The Function returned INCORRECT value ... \t\tFAILED\n\nFunction returned = " + str(
            output) + "\nbut\nExpected output is = " + str(expected_output) + "\n")
        exit()

    # Test-4: Testing the function apply_coder().
    output = encryption.find_best_shift(wordList, 'Ij, wpo oczmZ dn v OV ivhzy Vgqdi!')
    expected_output = 25
    if expected_output == output:
        comment("Test-4: The Function returned the correct value ...\t\tPassed\t(+10 points)")
        points += 10
    else:
        comment("Test-4: The Function returned INCORRECT value ... \t\tFAILED\n\nFunction returned = " + str(
            output) + "\nbut\nExpected output is = " + str(expected_output) + "\n")
        exit()

    # Test-5: Testing the function apply_coder().
    output = encryption.find_best_shift(wordList, 'CTnp')
    expected_output = 15
    if expected_output == output:
        comment("Test-5: The Function returned the correct value ...\t\tPassed\t(+10 points)")
        points += 10
    else:
        comment("Test-5: The Function returned INCORRECT value ... \t\tFAILED\n\nFunction returned = " + str(
            output) + "\nbut\nExpected output is = " + str(expected_output) + "\n")
        exit()

    # Test-6: Testing the function apply_coder().
    output = encryption.find_best_shift(wordList, 'Gwzsbqs vsGWhOHwcb ywburca rsgqsbR Fcibr')
    expected_output = 12
    if expected_output == output:
        comment("Test-6: The Function returned the correct value ...\t\tPassed\t(+10 points)")
        points += 10
    else:
        comment("Test-6: The Function returned INCORRECT value ... \t\tFAILED\n\nFunction returned = " + str(
            output) + "\nbut\nExpected output is = " + str(expected_output) + "\n")
        exit()

    # Test-7: Testing the function apply_coder().
    output = encryption.find_best_shift(wordList, 'fnjyxw knbrMnb vduCrYuRljcrxw jyyuH yxbbnbbxa frltnm')
    expected_output = 17
    if expected_output == output:
        comment("Test-7: The Function returned the correct value ...\t\tPassed\t(+10 points)")
        points += 10
    else:
        comment("Test-7: The Function returned INCORRECT value ... \t\tFAILED\n\nFunction returned = " + str(
            output) + "\nbut\nExpected output is = " + str(expected_output) + "\n")
        exit()

    # Test-8: Testing the function apply_coder().
    output = encryption.find_best_shift(wordList, 'heAd check Silk emPIrE sow faith reducTioN uniVersity sChool ear')
    expected_output = 22
    if expected_output == output:
        comment("Test-8: The Function returned the correct value ...\t\tPassed\t(+10 points)")
        points += 10
    else:
        comment("Test-8: The Function returned INCORRECT value ... \t\tFAILED\n\nFunction returned = " + str(
            output) + "\nbut\nExpected output is = " + str(expected_output) + "\n")
        exit()

    # Test-9: Testing the function apply_coder().
    output = encryption.find_best_shift(wordList, 'otzXujAik joyZGtik SOykxGhrk gshOzOut mGsk rKgjkxynOv mGxjkt Yzgot yoiq otyaxgtIk grutm nkgX vkxSoyyout Lxe mubkXtux')
    expected_output = 20
    if expected_output == output:
        comment("Test-9: The Function returned the correct value ...\t\tPassed\t(+10 points)")
        points += 10
    else:
        comment("Test-9: The Function returned INCORRECT value ... \t\tFAILED\n\nFunction returned = " + str(
            output) + "\nbut\nExpected output is = " + str(expected_output) + "\n")
        exit()

    # Test-10: Testing the function apply_coder().
    output = encryption.find_best_shift(wordList, 'gaugb hdvwVa fssxur')
    expected_output = 0
    if expected_output == output:
        comment("Test-10: The Function returned the correct value ...\tPassed\t(+10 points)")
        points += 10
    else:
        comment("Test-10: The Function returned INCORRECT value ... \t\tFAILED\n\nFunction returned = " + str(
            output) + "\nbut\nExpected output is = " + str(expected_output) + "\n")
        exit()

    # printing the total grade
    print()
    grade(points)
# run the test for find_best_shift()
# test_find_best_shift()

def test_decrypt_story():
    # todo
    pass
