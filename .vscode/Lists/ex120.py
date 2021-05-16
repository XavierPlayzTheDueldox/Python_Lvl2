#Ex 120 Is a List already in Sorted Order?
def readlist(lis):
    return sorted(lis)

    if readlist(numberslist) == numberslist:
        return True
    else:
        return False

def readnow():
    numberslist = list()
    ans = int(input('Enter your list inputs'))
    while ans != 0:
        #if ans == 0:
            #break
        numberslist.append(ans)
        ans = int(input('Enter your list inputs'))

print(readlist(readnow()))