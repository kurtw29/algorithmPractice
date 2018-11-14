def findPalindromeLength(index, arr):
    #odd palindrome
    trackerOdd = 1
    i = 1
    while(index-i >= 0 and index+i < len(arr)):
        if arr[index-i] == arr[index+i]:
            trackerOdd += 2
            i += 1
        else:
            break
    #even palindrome
    trackerEven = 0
    if index < len(arr)-1 and arr[index] == arr[index+1]:
        trackerEven += 2
        j = 1
        while(index-j >= 0 and index+1+j < len(arr)):
            if arr[index-j] == arr[index+1+j]:
                trackerEven += 2
                j += 1
            else:
                break
    if trackerOdd > trackerEven:
        return trackerOdd
    else:
        return trackerEven

def maxPalindrome(arr):
    max = {
        "index": 0,
        "length": 0
    }
    for i in range(len(arr)):
        # print(i, "and arr[i]: ", arr[i])
        p = findPalindromeLength(i, arr)
        # print("pLength: ",p)
        if p > max["length"]:
            max["index"] = i
            max["length"] = p
    if max["length"] > 1:
        if max["length"] % 2 != 0:
            output = arr[max["index"]]
            # print((max["length"]-1)/2)
            for j in range(1,int((max["length"]-1)/2)+1):
                output = arr[max["index"]-j] + output + arr[max["index"]+j]
            return output
        else: # max["length"] % 2 == 0 (even palindrome)
            output = arr[max["index"]] + arr[max["index"]+1]
            if max["length"]/2 - 1 > 0:
                for j in range(1,int((max["length"]/2))):
                    output = arr[max["index"]-j] + output + arr[max["index"]+1+j]
            return output
    else:
        "no palindrome found"

arr = "jjjjjjbcajacbjabaj"
print("string:", arr, "\nlongest palindrom: ",maxPalindrome(arr))
arr = "dbcqbbabad"
print("string:", arr, "\nlongest palindrom: ",maxPalindrome(arr))