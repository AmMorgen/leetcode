x = 122

def palindromo (x):
    invert = str(x)
    aocom = invert[::-1]
    if aocom == invert:
        return True
    else:
        return False
    