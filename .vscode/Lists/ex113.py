def readwords():
    ans = 'i'
    wordlist = list()
    while ans != '':
        ans = input('Enter your word. Enter a blank to proceed.').lower()
        if ans != '':
            wordlist.append(ans)
    return wordlist

def list_format(listinput):
    newlist = list()
    for i in range(len(listinput)-2):
        newlist.append(listinput[i])
        newlist.append(', ')
    newlist.append(listinput[-2])
    newlist.append(' and ')
    newlist.append(listinput[-1])
    return ''.join(newlist)

print(list_format(readwords()))