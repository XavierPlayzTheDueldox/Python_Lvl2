from ex104 import readval, sortedvalue

def removevalues(inp, n):
    return inp[n:-n]

if __name__ == '__main__':
    ans = readval('Enter a number. Enter a blank to proceed.', '')
    if len(ans) <= 3:
        print('Sorry, you have entered less than four numbers.')
    else:
        print(removevalues(sortedvalue(ans),int(input('Enter value of x:'))))
        print(ans)