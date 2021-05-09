def line_of_best_fit(linelist):
    b = linelist[1]
    rise = linelist[-1] - linelist[1]
    step = linelist[-2]
    m = rise / step
    return f'y = {m}x +{b}'

def readval():
    numberslist = list()
    ans=''
    while not ans=='':
        ans = input('Enter a number. Enter blank to proceed.')
        if ans != '':
            numberslist.insert(len(numberslist),int(ans))
    return numberslist

print(line_of_best_fit(readval())