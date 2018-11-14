def answer(l):
    # your code here
    if len(l) == 0:
        return 0
    #create largest # from #'s in l
    
    #case1
    #sum mod 3 == 0
    
    #otherwise:
        #find a number in the array == reminder (1 or 2) or (4 or 5) or (7 or 8)
        #find sum of number in array (skip 0,3,6,9)== reminder
        
        #remove that number or numbers
    
    #case2
    #reminder or reminder+3 or reminder+6 number exists in array
    
    #case 3
    #sum of array's two numbers == reminder
    
    #case 4 sum of all the array's number == 
    #if reminder, check if array has a number == reminder, remove that number from array
    #if cannot find reminder number in array, try finding a number while(reminder+3 < 10)
    #if there's sum that adds up to the reminder or reminder+3 < 10
        #skip if(# % 3 == 0 or # > reminder or 
    #otherwise no possible way to be divisible by 3
    
    sum = 0 #use to check divisble by 3 (sum % 3 == 0)
    for t in range(len(l)):
        min = l[t]
        for i in range(t+1,len(l)):
            if l[i] < min:
                l[t] = l[i]
                l[i] = min
                min = l[t]
        sum += l[t]
    # l is now sorted ascending order
    #function to convert array into the largest possible number
    def arrToNumber(arr):
        number = arr[0]
        for n in range(1,len(arr)):
            number += arr[n]*(10**n)
        return number
        
    reminder = sum % 3
    if reminder != 0: # array number is not divisible by 3
        while(reminder < 10):
            if reminder in l:
                l.remove(reminder) # array's number is now divisible by 3
                return arrToNumber(l)
            else:
                reminder+=3
    else:
        return arrToNumber(l)
    # #find the array elements whose sum == reminder
    reminder = sum % 3
    arr = []
    #find the two numbers in array that sums to reminder
    for n in l:
        print("n of l: ", n)
        if n % 3 != 0:
            if n < reminder or n < reminder+3 or n < reminder+6:
                if len(arr)>0:
                    for a in arr:
                        if a + n == reminder:
                            l.remove(a)
                            l.remove(n)
                            return arrToNumber(l)
                arr.append(n)
                print("arr: ", arr)
    # #write a function that takes an array and return an array that sums up to the remainder
    # def removeNum(arr, r):
    #     for inum in range(len(arr)):
    #         for item in range(inum+1,len(arr)):
                
    # #find three numbers in array that sums to reminder
    # while(item <= len(arr)
        
    # arr[0]+arr[1]+arr[2]
    # #find n < len(arr) numbers in array that sums to reminder
    # while(len(arr)>0):
    #     arr.pop(0)
    for remove in arr:
        l.remove(remove)
    if len(l) > 0:
        return arrToNumber(l)
    else:
        return 0
# # len(l) == 0, no possible number div by 3
    return 0

l = [7,7,9]
print(l)
print(answer(l))