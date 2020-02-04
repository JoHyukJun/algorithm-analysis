def IsPermutation(inFisrtStr, inSecondStr):
    if (len(inFisrtStr) != len(inSecondStr)):
        return False

    if (sorted(inFisrtStr) == sorted(inSecondStr)):
        return True
    else:
        return False

res = IsPermutation('doa', 'god')