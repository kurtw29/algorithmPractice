def binaryGap(N):
    print("N is ", N)
    if(N == 0 or N == 1):
        return 0
    # convert N into charArr[]
    charArr = []
    while(N >= 1):
        r = N % 2
        charArr.append(str(r))
        N = int((N - r)/2)
    print("Binary Array in reverse: ", charArr)
    binaryLength = 0
    # numGap = 0
    divider = 0
    Ocounter = 0
    for i in range(len(charArr)-1, 0, -1):
        print(charArr[i])
        if(charArr[i] == '1'):
            divider += 1
            if(Ocounter == 0 and divider % 2 == 0):
                divider = 1
            if(divider % 2 == 0 and divider != 0):
                # numGap += 1
                if(Ocounter > binaryLength):
                    binaryLength = Ocounter
                    print("Ocounter: ", Ocounter)
            Ocounter = 0
        else:
            Ocounter += 1
    return binaryLength

print("Testing")
print("binaryGap(0)", binaryGap(0))
print("binaryGap(1)", binaryGap(1))
print("binaryGap(2)", binaryGap(2))
print("binaryGap(5)", binaryGap(5))
print("binaryGap(10)", binaryGap(10))
print("binaryGap(35)", binaryGap(35))
print("binaryGap(100)", binaryGap(100))

