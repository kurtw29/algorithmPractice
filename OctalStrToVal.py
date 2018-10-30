def Dec2Oct(value):
    r = ""
    if(value < 8):
        return str(value) + r
    else:
        r = str(value % 8) + r
        val = int((value - value % 8) / 8)
        if( val < 8):
            return str(val) + r
        else:
            return str(Dec2Oct(val)) + r


print("Dec2Oct(1): ",Dec2Oct(1))
print("Dec2Oct(10): ",Dec2Oct(10))
print("Dec2Oct(65): ",Dec2Oct(65))
print("Dec2Oct(100): ",Dec2Oct(100))
