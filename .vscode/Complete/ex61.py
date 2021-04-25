firstno = float(input('Enter a number:'))

if firstno == 0:
    print('Sorry, an Error has Occured.')

else:
    count = 1
    no = 1

    while no != 0:
        no = float(input('Enter a number:'))
        if no != 0:
            count = count + 1
            avg = (firstno + no) / count
            firstno = firstno + no
        else:
            print(f'The Average of your {count} number(s) is {avg}.')


