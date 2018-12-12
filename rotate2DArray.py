def rotate2DArray(arr):
    n = len(arr)
    if n == 1:
        return arr
    temp = arr[0][0]
    print("math.floor(n/2)= ",math.floor(n/2))
    for i in range(0,n//2):
        for j in range(i,n-i-1):
            temp = arr[i][j]
            arr[i][j] = arr[n-j-1][i]
            arr[n-j-1][i] = arr[n-i-1][n-j-1]
            arr[n-i-1][n-j-1] = arr[j][n-i-1]
            arr[j][n-i-1] = temp
    return arr

ar5 = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]
ar4 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
ar3 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
ar2 = [
    [1,2],
    [3,4]
]
ar1 = [161]
# print(rotate2DArray(ar1))
# print("*"*15)
# print(rotate2DArray(ar2))
# print("*"*15)
# print(rotate2DArray(ar3))
# print("*"*15)
# print(rotate2DArray(ar4))
# print("*"*15)
for x in range(0,len(ar5)):
    print(ar5[x])
print("*"*15)
rotate2DArray(ar5)
for x in range(0,len(ar5)):
    print(ar5[x])
