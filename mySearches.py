'''
Zachary Sisco, Unit 4 Assignment 2
mySearches

This program will serve as a library containing two functions, one to execute
a binary search and another to execute a linear search. This library will be
imported into the lookup.py program.
'''

#create binary search algorithm
def bsearch(num, numlist):

    low = 0
    high = len(numlist) - 1
    item = 0
    c = 0

    #execute the search, adjust search size and step counter
    while low <= high:

        mid = (low+high) // 2
        item = numlist[mid]
        
        if num == item:
            c = c + 1
            print("Number Found: ", item)
            print("Steps Taken in Binary Search: ",c)
            return "Found at Index " , mid

        elif num < item:
            high = mid - 1
            c = c + 1

        else:
            low = mid + 1
            c = c + 1
            
    #number not found 
    print("Number",num,"not found, I looked ",c,"times")        
    return -1

#create linear search algorithm
def lsearch(num, numlist):

    c = 0

    #execute search, adjust counter
    for i in range(0, len(numlist)-1):
        
        if num == numlist[i]:
            c = c + 1
            print("Number Found: ", numlist[i])
            print("Steps Taken in Linear Search: ",c)
            return "Found at Index ", i
        
        else:
            c = c + 1
            
    #number not found
    print("Number",num,"not found, I looked ",c,"times")
    return -1

