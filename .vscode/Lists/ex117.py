def line_of_best_fit(x,y):
    sx = sum(x)
    sy = sum(y)
    sxy = 0

    sxsq = 0
    for i in range(len(x)):
        sxsq += x[i] ** 2
    sxsq2 = sum(x) ** 2
    n = len(x)

    for i in range(len(x)):
        sxy += x[0] * y[0]
        x.pop(0)
        y.pop(0)

    m = (sxy - ((sx*sy)/n))
    m /= (sxsq - (sxsq2/n))

    b = (sy/n) - (m * (sx/n))

    return f'y = {m:.2f}x +{b:.1f}'


x = list()
y = list()
ans=1
while not ans=='':
    ans = input('Enter a number. Enter blank to proceed.')
    if ans != '':
        x.insert(len(x),float(ans))
    if ans == '':
        break
    ans = input('Enter a number. Enter blank to proceed.')
    if ans != '': 
       y.insert(len(y),float(ans))


print(line_of_best_fit(x, y))