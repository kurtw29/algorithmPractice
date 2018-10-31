print("*"*12,"Print 1-255","*"*10)
# Print all the integers from 1 to 255
output = " "
def print1to255():
    output = ""
    for i in range(1, 256):
        output = output + " " + str(i)
    return output
# print(print1to255())

print("*"*12,"Print 0-255 and Sum", "*"*10)
# Print integers from 0 to 255, and the sum so far
def printIntsAndSum0to255():
    sum = 0
    output = ""
    for i in range(0, 256):
        sum = sum + i
        output = output+", "+ "(#: "+ str(i)+ " sum: "+ str(sum)+")"
    return output
# print(printIntsAndSum0to255())

print("*"*12, "Max of Array", "*"*12)
# Print the largest element in a given array, by iterating through it and comparing values
def printMax(arr):
    if len(arr) == 0:
        return None
    else:
        max = arr[0]
        for i in range (1, len(arr)):
            if max < arr[i]:
                max = arr[i]
    return max
arr = [-20,-1,2,3,0]
# print(printMax(arr))

print("*"*12, "Print Odds 1-255","*"*12)
# Print all odd integers from 1-255.
def oddInt1To255():
    output = "1"
    for i in range (3 ,255+1, 2):
        output = output + ", " + str(i)
    return output
# print(oddInt1To255())

print("*"*12, "returns odd array 1-255","*"*12)
# Create an array with odd integers from 1-255.
def oddArray():
    arr = []
    for i in range(1,255+1):
        if(i % 2 !=0):
            arr.append(i)
    return arr
# print(oddArray())

print("*"*12, "print Array Values","*"*12)
# Print all values in a given arrays by iterating through it.
def printArrVal(arr):
    output = ""
    for i in range(0,len(arr)):
        output = output + ", " + str(arr[i])
    return output
hello = 'hi'
arr = ["hello", 2, -1, "yes please", 0, hello]
# print(printArrVal(arr))

print("*"*12, "Print Average of Array","*"*12)
# Analyze an array's values and print the average.
def averageArr(arr):
    sum = arr[0]
    for i in range(1, len(arr)):
        sum += arr[i]
    return sum/len(arr)
arr = [5, 4, 3, 2, 1]
# print(averageArr(arr))

print("*"*12, "Greater Than Y","*"*12)
# Count and print the number of array values less than a given Y.
def countPrintArrLessY(arr, Y):
    counter = 0
    output = ""
    for i in range( 0, len(arr)):
        if arr[i] < Y:
            counter += 1
            output = output + " " + str(arr[i])
    return "counter: " + str(counter) + ", {" + output + "}"
arr = [1,2,3,4,5,6,7]
num = 4
# print(countPrintArrLessY(arr, num))

print("*"*12, "Print Max, Min, Average Array Value", "*"*12)
# Given an array, print Max, Min, and Average of array values.
def MaxMinAve(arr):
    max = min = sum = arr[0]
    for i in range( 1, len(arr)):
        if arr[i] > max:
            max = arr[i]
        else:
            if arr[i] < min:
                min = arr[i]
        sum += arr[i]
    return "Max: "+ str(max)+", Min: "+ str(min) + ", Average: " + str(sum/len(arr))
arr = [1, 2, 3, 4, 5]
# print(MaxMinAve(arr))

print("*"*12, "Square Array Values","*"*12)
# Given an array, square each array values in the array.
def sqArr(arr):
    for i in range( 0, len(arr)):
        arr[i] *= arr[i]
    return arr
arr = [1,2,3,4,5]
# print(sqArr(arr))

print("*"*12, "Zero out array Negative values","*"*12)
# Set negative array values to 0.
def zeroNeg(arr):
    for i in range( 0, len(arr)):
        if arr[i] < 0:
            arr[i] = 0
    return arr
arr = [-1, 0, 2, 3, -12]
# print( zeroNeg(arr) )

print("*"*12, "Shift arrays values left", "*"*12)
# Shift array values. Drop the first array values and leave "0" at end.
def shiftArrLeft(arr):
    for i in range( 0, len(arr)):
        if i != len(arr) - 1:
            arr[i] = arr[i+1]
        elif i == len(arr) - 1:
            arr[i] = 0
    return arr
arr = [1,2,3,4,5]
# print(shiftArrLeft(arr))

print("*"*12, "Swap string for Array Negative Values", "*"*12)
# Replace any negative array values with "Dojo"
def swapNegDojo(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = "Dojo"
    return arr
arr = [1,2,-1,0,-20, 0]
print(swapNegDojo(arr))