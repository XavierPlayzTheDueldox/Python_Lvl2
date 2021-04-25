cp = input('Please Enter your car liscence plate number:')

lol = list(cp)

if lol[0] != 1 or lol[0] != 2 or lol[0] != 3 or lol[0] != 4 or lol[0] != 5 or lol[0] != 6 or lol[0] != 7 or lol[0] != 8 or lol[0] != 9:
    typ = 'old'
else:
    typ = 'new'


if typ == 'old':
    print('You need to renew your liscence plate number.')
else: 
    print('You are safe as your liscence plate is valid and does not require and renewal.')