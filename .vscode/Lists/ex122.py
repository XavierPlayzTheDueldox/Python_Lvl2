def bel_abv_avg(numlist,average):
    bel, abv, avg, finallist = list(), list(), list(), list()
    for i in numlist:
        if numlist[i] > average:
            abv.append(numlist[i])
        elif numlist[i] < average:
            bel.append(numlist[i])
        else:
            avg.append(average)
    finallist.append('Below Average:')
    for i in bel:
        finallist.append(bel[i])
    finallist.append('Average')
    for i in avg:
        finallist.append(average)
    finallist.append('Above Average')
    for i in abv:
        finallist.append(abv[i])
    return (*finallist, sep == "\n")

inp = readval('Enter a number. Enter 0 to proceed.', '0')
print(bel_abv_avg(inp, avg_reader(inp)))