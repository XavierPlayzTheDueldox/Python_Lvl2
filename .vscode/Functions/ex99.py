def dec2arb(num,base):
    arbitrary = ''
    quotient = num
    while quotient > 0:
        remainder = quotient % base
        arbitrary += str(quotient % base)
        quotient = (quotient // base)
    arbitrary = arbitrary[::-1]
    return arbitrary

def arb2dec(num_str,base):
    decimal = 0
    for i in num_str:
        decimal = decimal * base + int(i)
    return decimal

base1 = int(input('Enter the base of input.'))
base2 = int(input('Enter the base of output.'))
ans1 = input('Enter the input.')

print(dec2arb(arb2dec(ans1,base1),base2))