#Gets input from the user
d = int(input('Enter the day:'))
y = int(input('Enter the Year:'))
m = int(input('Enter the month:'))


#Checks if year is a leap year
if y % 400 == 0:
    typ = 'leap'
elif y % 100 == 0:
    typ = 'notleap'
elif y % 4 == 0:
    typ = 'leap'
else:
    typ = 'notleap'


#Adjusts Year
cy = y


#Adjusts month
if m == 12 and d == 31:
    cm = 1
    cy = y + 1
else:
    cm = m


#Adjusts day (And month if necessary)
if d == 30 and m == 4 or m == 6 or m == 9 or  m == 11:
    cd = 1
    cm = m + 1
elif d == 31 and m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10:
    cd = 1
    cm = m + 1
elif typ == 'leap' and m == 2 and d == 28:
    cd = 29
elif typ == 'leap' and m == 2 and d == 29:
    cd = 1
    cm = m + 1
else:
    cd = d + 1


print(f'{cd}-{cm}-{cy}')