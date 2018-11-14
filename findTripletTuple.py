def answer(l):
    # your code here
    # if lk % lj == 0 and lj % li == 0
    
    #sort given array
    #loop array starting from highest number of array (lk) to lowest number
    #nested loop starting from index after (lk) and find number (lj) s.t. lk % lj ==0 
    #once found (lj), start loop starting from index after (lj) to find number (li) s.t. lj % li == 0
    # once found (li), add to tupArr.push((li, lj, lk)) and continue the loop
    # at end of triple-nested loop - return len(tupArr)
    if len(l)<3:
        return 0
    tupArr = []
    # l.sort(reverse=True)
    for indxLk in range(len(l)):
        for indxLj in range(indxLk+1, len(l)):
            if l[indxLk] % l[indxLj] == 0:
                for indxLi in range(indxLj+1, len(l)):
                    if l[indxLj] % l[indxLi] == 0:
                        tupArr.append([l[indxLi], l[indxLj], l[indxLk]])
    return len(tupArr)

def answer2(l):
    if len(l)<3:
        return 0
    tupArr = []
    l.sort()
    for indxLi in range(len(l)):
        for indxLj in range(indxLi+1, len(l)):
            if l[indxLj] % l[indxLi] == 0:
                for indxLk in range(indxLj+1, len(l)):
                    if l[indxLk] % l[indxLj] == 0:
                        tupArr.append([l[indxLi], l[indxLj], l[indxLk]])
        return len(tupArr)
    return 0

def answer3(l):
    if len(l)<3:
        return 0
    tupArr = []
    for k in range(len(l)-1, 0, -1):
        iArr = []
        for i in range(k-1, -1, -1):
            if l[k] % l[i] == 0:
                iArr.insert(0,l[i])
        if len(iArr) > 1: # there's a possibly of lj
            for j in range(len(iArr)-1, 0, -1):
                for i in range(j-1, -1, -1):
                    if iArr[j] % iArr[i] == 0: # there's a lj
                        tupArr.append([iArr[i], iArr[j], l[k]])
    return len(tupArr)  

def answer4(l):
    if len(l)<3:
        return 0
    tupArr = []
    jObj = {}
    indxLj = {}
    # l.sort()
    for j in range(len(l)-2, 0, -1):
        # find all the possible li for each lj:
        iArr = []
        for i in range(j-1, -1, -1):
            if l[j] % l[i] == 0 and l[i] not in iArr: # avoid duplicating li's
                iArr.insert(0,l[i])
        if len(iArr) > 0:
            jObj[l[j]] = iArr # all the possible unique li in an array of a lj
            indxLj[j] = l[j] # track lj's index in l-array
    kObj = {}
    counter = 0
    for k in range(len(l)-1, 1, -1):
        # find all possible lj for each lk:
        jArr = []
        for j in indxLj: # all the index of lj with possibility of making triple
            if l[k] % l[j] == 0 and k > j: # a lj that may make a lucky triple
                if l[k] not in kObj or l[j] not in kObj[l[k]]: # prevent duplicate 
                    print("l[k]:", l[k], ", l[j]:", l[j], ", jobj[l[j]]:", jObj[l[j]] )
                    jArr.append(l[j]) # this lj is acceptable for a lucky triple
                    kObj[l[k]] = jArr # associate the lk with a lj-array
                    counter += len(jObj[l[j]]) # the number of unique li associated with this lj = number of lucky triple we can make for this one lk
                    # tupArr.append()
                    print("counter: ",counter)
    return counter

def answer5(l):
    obj = {} # keep track of lj (key of obj) and li (value of obj)
    counter = 0 #keep track of number of lucky triple
    # for each element in the list:
    for li in l:
        #check element's value is found in keys of obj - it means the element is divisble by an previous element
        if li in obj:
            #if that previous element is also divisble by an earlier element, we found a lucky triple (the current element = lk, the associated key = lj, the associated key's value's obj = li)
            if len(obj[li]) > 0 and obj[li].count(li) < 2:
                counter += 1 #counting number of Lucky triples
            #if there's no additional previous element found, then we found a lj, add to its list of values (in case same number appear again, and we'll then be able to make a lucky triple)
            obj[li].append(li)
        else:
        #element value not found in keys of obj - means first time seeing this number - add this element to our keys of obj
            obj[li] = []
            # then check divisbility with each of all others keys of obj to see if this element value makes a lucky triple or not
            for objKey in obj:
                #check if element value is divisible by any keys in obj and be sure not to include the key we just added to avoid duplicate
                if li % objKey == 0 and li != objKey: 
                    #found the key - then check if it has already been divisble by other values
                    if len(obj[objKey]) > 0 and obj[objKey].count(objKey) < 2:
                        counter += 1 #found a lucky triple b/c the key obj was also divisible by another previous number
                    #key of obj is not divisble by another previous number, but it is now, append for future lucky triple
                    obj[li].append(objKey)
    return counter #PROBLEM
            
def answer6(l):
    count = 0
    arrCheck = [0] * len(l)
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if l[j] % l[i] == 0:
                arrCheck[j] += 1
                count += arrCheck[i]
    return count

# l = [1,1,1]
# print("*"*12, "case 1: l: ", l)
# print(answer5(l))
# l = [1,2,3,4,5,6]
# print("*"*12, "case 2: l: ", l)
# print(answer5(l))
# l = [1,1,1,1,1]
# print("*"*12, "case 3: l: ", l)
# print(answer5(l))
# l = [5,5,5,1,1,1]
# print("*"*12, "case 4: l: ", l)
# print(answer5(l))
# l = [6,5,4,3,2,1]
# print("*"*12, "case 5: l: ", l)
# print(answer5(l))
l = [1,2,4,4,8,16]
print("*"*12, "case 6: l: ", l)
print(answer6(l))