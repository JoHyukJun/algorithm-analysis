'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


def IsUniqueChars(inStr):
    if (len(inStr) > 128):
        return False

    charSet = [0] * 128

    for i in range(0, len(inStr)):
        val = ord(inStr[i])

        if (charSet[val]):
            return False
        
        charSet[val] = True
    
    return True
