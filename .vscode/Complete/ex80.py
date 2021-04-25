from random import *
Average, rounds = 0, 0
def flip_one_round():
    global rounds, Average
    prevf, prevprevf, coin_flip, numflips = '0', '1', '2', 0
    while True:
        numflips+=1
        if randint(1,2) == 1:
            coin_flip = 'H'
        else:
            coin_flip = 'T'
        print(coin_flip,' ', end="")
        if prevf == prevprevf == coin_flip:
            break
        prevprevf, prevf = prevf, coin_flip
    print(f'({numflips} flips)')
    rounds += 1
    Average = numflips + Average
    

for i in range(10):
    flip_one_round()
Average = Average / rounds
print(f'It took an Average of {Average}.')