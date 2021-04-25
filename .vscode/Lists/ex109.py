def listofpd(number):
    newlist = list()
    for i in range(1,number//2+1):
        if number % i == 0:
            newlist.append(i)
    return newlist

if __name__ == "__main__":
    number = int(input('Enter a number:'))
    print(listofpd(number))
