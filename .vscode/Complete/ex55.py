fn = float(input('Enter the Frequency number'))

if fn < 3e9: 
    print('Radio waves!')
elif fn < 3e12:
    print('Microwaves!')
elif fn < 4.3e13:
    print('Infrared light!')
elif fn < 7.5e14:
    print('Visible Light!')
elif fn < 3e17:
    print('Ultraviolet Light!')
elif fn < 3e19:
    print('X-rays')
else:
    print('Gamma rays!')

