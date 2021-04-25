letters = list('0123456789ABCDEF')
inp = ''

def hex2int(inp):
    global letters
    if inp in letters:
        if not inp.isdigit():
            inp = inp.upper()
        return letters.index(inp)
    else:
        return None

def int2hex(inp):
    global letters
    if inp >= 1 and inp <= 15:
        return letters[inp]
    else:
        return None

#Main Code

if __name__ == "__main__":
    choice = input("Enter 1 to use hexadecimal to decimal converter. Enter 2 to use decimal to hexadecimal converter.")
    if choice == '1':
        inp = input('Enter your Hexadecimal:')
        print(hex2int(inp))
    elif choice == '2':
        inp = int(input('Enter your Decimal:'))
        if inp.isdigit():
            print(int2hex(inp))
        else:
            print('Sorry, the input is not an integer (decimal). Please try again.')
    else:
        print("You have not inputted 1 or 2. PLease run the project again to use it.")