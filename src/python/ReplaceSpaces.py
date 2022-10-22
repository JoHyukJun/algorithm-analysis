'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


def ReplaceSpaces(inStr, trueLength):
    spaceCoount = 0
    index = 0

    res = inStr.replace(' ', '%20')

    return res

res = ReplaceSpaces('Mr John Smith', 13)
print(res)