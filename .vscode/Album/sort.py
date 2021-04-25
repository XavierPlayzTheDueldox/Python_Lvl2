#1. sortedvalue()
#sortedvalue() returns a sorted order of the list input
def sortedvalue(listofnum):
    for i in range(len(listofnum)):
        listofnum[i] = int(listofnum[i])
    return sorted(listofnum)

#2. reverseorder()
#reverseorder() returns a reverse sorted order of the list input
def reverseorder(inp):
    newlist = list()
    for i in range(len(inp)):
        newlist.append(inp[-1])
        inp.remove(inp[-1])
    return newlist

#3. removevalues()
#removevalues() returns a list with
def removevalues(inp):
    return inp[2:-2]

def removeduplicates(listofwords):
    newlist = list()
    while not listofwords == list(''):
        if not newlist.__contains__(listofwords[0]):
            newlist.append(listofwords[0])
        listofwords = listofwords[1:len(listofwords)]
    return newlist

def negzerpos(numberslist):
    neglist, poslist, zerlist, finallist = list(), list(), list(), list()
    while not numberslist == list(""):
        if numberslist[0] < 0:
            neglist.append(numberslist[0])
        elif numberslist[0] > 0:
            poslist.append(numberslist[0])
        else:
            zerlist.append(numberslist[0])
        numberslist = numberslist[1:len(numberslist)]
    finallist = neglist
    for i in range(len(zerlist)):
        finallist.append(0)
    while poslist != list(''):
        finallist.append(poslist[0])
        poslist = poslist[1: len(poslist)]
    return finallist

def listofpd(number):
    newlist = list()
    for i in range(1,number//2+1):
        if number % i == 0:
            newlist.append(i)
    return newlist

def perf_num(number, listofnum):
    numsum = 0
    for i in range(len(listofnum)):
        numsum += listofnum[i]
    return numsum == number