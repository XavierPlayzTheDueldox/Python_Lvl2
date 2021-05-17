def tokenize(new):
    newstr = list()
    adder = ''
    inp = list()
    for i in range(len(new)):
        if new[i] != ' ':
            inp.append(new[i])
    for i in range(len(inp)):
        adder = inp[i]
        if adder == '+' or '-':
            if inp[i-1].isdigit():
                adder = inp[i-1:i+2]
                i += 1
            if inp[i-1] == ")":
                adder = inp[i-1:i+2]
                i += 1
            else:
                adder = inp[i]
        newstr.append(adder)
    return newstr

inp = input('Enter your number:')



print(tokenize(new))