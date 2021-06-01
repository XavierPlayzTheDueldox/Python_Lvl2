def isSublist(sublistinp, listinp):
    if listinp.__contains__(sublistinp):
        return True
    else:
        return False

if __name__ == '__main__':
    smaller, larger = str(), str()
    ans = input('Enter your number (Smaller). 0 to exit')
    while ans != '0':
        smaller += ans
        ans = input('Enter your number (Smaller). 0 to exit')

    ans = input('Enter your number (Larger). 0 to exit')
    while ans != '0':
        larger += ans
        ans = input('Enter your number (Larger). 0 to exit')

print(isSublist(smaller, larger))