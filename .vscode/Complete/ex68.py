print(f'{"":=^48}')
print(f'{"PARITY BIT GENERATOR":^48}')
print(f'{"":=^48}')
code = 0
while code != '':
    code = input('Enter your 8-bit data:')
    if code == '':
        break
    code = list(code)
    x = code.count('1')
    length = len(code)
    if length != 8:
        print('This is not a set of 8-Bits.')
    elif x % 2 == 0:
        print('Parity bits: 1')
    else:
        print('Parity bits: 0')

    
