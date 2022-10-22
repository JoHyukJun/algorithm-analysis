'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


def IsPermutation(inFisrtStr, inSecondStr):
    if (len(inFisrtStr) != len(inSecondStr)):
        return False

    if (sorted(inFisrtStr) == sorted(inSecondStr)):
        return True
    else:
        return False

res = IsPermutation('doa', 'god')