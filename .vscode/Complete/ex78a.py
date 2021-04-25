decimal = int(input('Enter a decimal to convert:'))
binary = ''

while decimal > 0:
    binary = str(decimal % 2) + binary
    decimal = decimal // 2

print('Binary:', binary)