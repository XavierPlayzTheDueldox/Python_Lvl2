#Ex 120 Is a List already in Sorted Order?
def readval():
    numberslist, ans = list(), int(input('Enter a number. Enter 0 to proceed.'))
    while ans != 0:
        numberslist.append(ans)
        ans = int(input('Enter a number. Enter 0 to proceed.'))
    return numberslist

def check(numberslist):
    if sorted(numberslist) == numberslist:
        return True
    else:
        return False

print(check(readval()))