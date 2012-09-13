import math

def isPrime(n):
    if(not n%2):
        return 0
    sqn = int(math.ceil(math.sqrt(n)))
    for i in range(3,sqn+1,2):
        if(not n%i):
            return 0
    return 1

def main():
    guess,count,limit = 3,2,10001
    while(count < limit + 1):
        if isPrime(guess):
            count += 1
        guess += 2
    print guess-2

main()
