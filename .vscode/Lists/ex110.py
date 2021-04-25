from ex109 import listofpd

def perf_num(number, listofnum):
    numsum = 0
    for i in range(len(listofnum)):
        numsum += listofnum[i]
    return numsum == number

ans = int(input('Enter an integer:'))
print(perf_num(ans, listofpd(ans)))
