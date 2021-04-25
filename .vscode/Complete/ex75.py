m = int(input('Enter a number:'))
n = int(input('Enter a second number:'))
d=0
if n>m:
    d=m
else:
    d=n
print(d)
while (m%d)!=0 or (n%d)!=0:
    d-=1
print(f'{d} is the greatest common divisor of the two numbers.')