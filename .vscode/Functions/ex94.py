from random import *
def randpassword():
    password = ''
    for i in range(randint(7,10)):
        password += chr(randint(33,126))
    return password

if __name__ == '__main__':
    print(randpassword())