def readwords():
    ans = 'i'
    wordlist = list()
    while ans != '':
        ans = input('Enter your word. Enter a blank to proceed.').lower()
        if ans != '':
            wordlist.append(ans)
    return wordlist

def removeduplicates(listofwords):
    newlist = list()
    while len(listofwords) != 0:
        if not listofwords[0] in newlist:
            newlist.append(listofwords[0])
        listofwords = listofwords[1:len(listofwords)]
    return newlist

print(removeduplicates(readwords()))
