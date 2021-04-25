wl = float(input('Enter the Wavelength.'))

if wl > 750 or wl < 380:
    print('Your number is either too high or too low!')
else:
    if wl >= 620:
        print('Red')
    elif wl >= 590:
        print('Orange')
    elif wl >= 570:
        print('Yellow')
    elif wl >= 495:
        print('Green')
    elif wl >= 450:
        print('Blue')
    else:
        print('Violet')