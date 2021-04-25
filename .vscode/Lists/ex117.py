def readval(msg, code):
    numberslist = list()
    ans = input(msg)
    while ans != code:
        numberslist.append(ans)
        ans = input(msg)
    return numberslist

def sortedvalue(listofnum):
    for i in range(len(listofnum)):
        listofnum[i] = int(listofnum[i])
    return sorted(listofnum)



if __name__ == '__main__':
    listval = sortedvalue(readval('Enter a number. Enter 0 to proceed.', '0'))
    print(*listval, sep = "\n")