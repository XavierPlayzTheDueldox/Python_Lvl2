def prime(num):
    if num > 1:
        for i in range(2, num//2):
            if (num % i) == 0:
                return False
                break
            else:
                return True
    else:
        return False

if __name__ == "__main__":
    no = int(input('Enter a number to check if it is prime:'))
    print(prime(no))