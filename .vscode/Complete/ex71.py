x = int(input('Enter a number:'))
guess = x / 2
while ((guess * guess) - x) > 10e-12:
    guess = (guess + (x/guess))/2
print(guess)