def readval(msg, code):
    numberslist = list()
    ans = input(msg)
    while ans != code:
        numberslist.append(ans)
        ans = input(msg)
    return numberslist

def readwords():
    ans = 'i'
    wordlist = list()
    while ans != '':
        ans = input('Enter your word. Enter a blank to proceed.').lower()
        if ans != '':
            wordlist.append(ans)
    return wordlist

def askint():
    return int(input('Enter an integer:'))

def askstr():
    return input('Enter an integer:')