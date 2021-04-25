from ex92 import prime

def nextPrime(inte):
    inte += 1
    while not prime(inte):
        inte += 1
    return inte

integer = int(input('Enter a number:'))
print(f"The Next Prime is {nextPrime(integer)}")