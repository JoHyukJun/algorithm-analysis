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
