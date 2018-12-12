def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    # test cases:
#           m(0,0), m(1,0), m(1000, 0)
#           m(100, 100), m(1, 90), m(90,1)
    #
    numDict = {
        "0":0,
        "1":1,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9
    }
    intArr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if len(num1) == 0 or len(num2) == 0:
        return "invalid arguments"
    
    # num1Int = num1[len(num1)-1]
    # num2Int = num2[len(num2)-1]
    
    if len(num1) == 1:
        if num1 == "0":
            return "0"
        elif num1 == "1":
            return num2
    elif len(num2) == 1:
        if num2 == "0":
            return "0"
        elif num2 == "1":
            return num1
    # else:       # len(num1) > 1 and len(num2) > 1
    num1Int = 0
    for i in range(len(num1)-1, -1, -1):
        num1Int += numDict[num1[i]]*(10**(len(num1)-1-i))
    num2Int = 0
    for j in range(len(num2)-1, -1, -1):
        num2Int += numDict[num2[j]]*(10**(len(num2)-1-j))
    outputInt = num1Int*num2Int
    wOne = 1
    wTwo = 10
    mod = outputInt % wTwo
    output = intArr[mod]
    outputInt -= mod
    wOne *= 10
    wTwo *= 10
    while(outputInt > 0):
        mod = outputInt % wTwo
        print(mod)
        output = intArr[mod//(wOne)] + output
        wOne *= 10
        wTwo *= 10
        outputInt -= mod
    return output
        # if len(num1) >= len(num2):
        #     for i in range(len(num1)-1,-1,-1):
        #         num1Int += numDict[num1[i]]*(10**(len(num1)-1-i))
        #     for j in range(len(num2)-1,-1,-1):
        #         num2Int += numDict[num2[j]]*(10**(len(num2)-1-j))
        #     numOutput = num1Int * num2Int
        # else:
print(multiply("10","1"))
print(multiply("1","10"))
print(multiply("10","10"))
print(multiply("2","3"))