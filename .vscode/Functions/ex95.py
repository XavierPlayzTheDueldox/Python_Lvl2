from random import *
def liscence():
    lis = ''
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nums = '1234567890'
    for i in range(randint(2,3) + 1):
            lis += chars[randint(0,25)] 
    for i in range(3):
            lis += nums[randint(0,9)]
    return lis



print(liscence())