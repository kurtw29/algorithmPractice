#Given a string, find the longest substring without repeating character

def nonRepeatSubstring(stri):
    #find all the unique character in the string
    substring = ""
    ss = ""
    for i in range(len(stri)):
        print("i: ",i, " substring: ", substring)
        charCheckArr = set()
        ss = ""
        print("charCheckerArr: ", charCheckArr)
        for s in range(i, len(stri)):
            print("stri[s]: ", stri[s], ", ss", ss, ", charCheckerArr: ", charCheckArr)
            if stri[s] in charCheckArr:
                print("len(ss)", len(ss), "len(substring)", len(substring))
                break
            else:
                charCheckArr.add(stri[s])
                ss = ss+stri[s]
                if len(ss) > len(substring):
                    substring = ss
    return substring

testString = "helloworld"
print("testString: ", testString, "output: ",nonRepeatSubstring(testString))
