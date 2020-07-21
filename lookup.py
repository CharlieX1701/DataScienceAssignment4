'''
Zachary Sisco, Unit 4 Assignment 2

The purpose of this assignment is to read in a list of 10000 random numbers,
clean and sort the data, and then run a binary and a linear search through the
data for a specified number. The code for the binary and linear searches will
be imported from a libray. If the specified number is in the data, the search
will return the index of the number in the list as well as the number of steps
needed to find the number. If the number is not in the list, then the search
will return -1.
'''

#import lib
import mySearches

#take in data, read it, clean it, turn to int, sort it
def getData(num):

    nf = open('rands.txt' , 'r')
    data = nf.read()
    nf.close()

    data = data.replace('\n', '\t')
    data = data.split('\t')

    for i in range(0, len(data)):
        data[i] = int(data[i])

    data.sort()
    
    return data

#conduct search through data
def search():
    
    searchList = [78700, 3333, 1118]

    for i in searchList:
        print(mySearches.bsearch(i, dataList),'\n')
        print(mySearches.lsearch(i, dataList),'\n')
        print("########################\n")

#global variable to use in search
dataList = getData(1120)
search()

#end with note of positivity 
print("The harder you work for something, the greater you'll feel when you achieve it.")
