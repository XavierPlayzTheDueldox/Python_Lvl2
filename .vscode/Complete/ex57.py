year = int(input('Please Enter the year:'))

if year % 400 == 0:
    typ = ''
elif year % 100 == 0:
    typ = ' not'
elif year % 4 == 0:
    typ = ''
else:
    typ = ' not'



print(f'Your Year is{typ} a leap year.')