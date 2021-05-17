def countRange(max, min, numberslist):
    numberslist = sorted(numberslist)
    extra = list()
    for i in range(len(numberslist)):
        if numberslist[i] <= min:
            extra.append(numberslist[i])
        elif numberslist[i] >= max:
            extra.append(numberslist[i])
    return len(extra) - 2

def readval():
    numberslist, ans = list(), int(input('Enter a number. Enter 0 to proceed.'))
    while ans != 0:
        numberslist.append(ans)
        ans = int(input('Enter a number. Enter 0 to proceed.'))
    return numberslist

max = int(input('Enter maximum'))
min = int(input('Enter minimum'))
print(countRange(max,min,readval()))