def password(inp):
    #Sets Variables
    upcheck, locheck, numcheck, symcheck, upperchars, lowerchars, numbers, symbols = False, False, False, False, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz', '1234567890','!#$%&()*+,-./:;<=>?@[\]^_`{|}'
    #checks if characters is at least 8
    if len(list(inp)) >= 8:
        #checks for the conditions of a password
        for i in range(len(inp)):
            if inp[i].isupper():
                upcheck = True
            if inp[i].islower():
                locheck = True
            if inp[i].isdigit():
                numcheck = True
            if inp[i] in symbols:
                symcheck = True

    #if all are true, returns true
    return upcheck and locheck and numcheck and symcheck

if __name__ == '__main__':  
    #main code
    inp = list(input('Enter a password'))
    print(password(inp))
