def string_central(string,width):
    global pad 
    width //= 2
    for i in range(width):
        pad = pad + ' '
    return pad + string

pad = ''
stri = input('Enter your String to Centralise:')
wid = int(input('Enter the number of spaces to centralise it in:'))
print(string_central(stri,wid))