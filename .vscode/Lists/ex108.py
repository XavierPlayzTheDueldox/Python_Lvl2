def readval():
    numberslist = list()
    ans=1
    while not ans=='':
        ans = input('Enter a number. Enter blank to proceed.')
        if ans != '':
            numberslist.insert(len(numberslist),int(ans))
    return numberslist

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

print(negzerpos(readval()))