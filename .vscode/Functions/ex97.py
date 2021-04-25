from ex96 import password
from ex94 import randpassword

def randpass():
    check, passw = 0, ''
    while not password(passw):
        passw = randpassword()
        password(passw)
        check+=1
    return passw, check


passw, check = randpass()
print(f'It took {check} try/tries to generate your good password.')
print(f'Your password is {passw}')