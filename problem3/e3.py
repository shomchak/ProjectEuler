# Starting with 2, find new primes and divide into the number.

def divideOut(N,p):
    if N%p == 0:
        return divideOut(N/p,p)
    else:
        return N

def main():
    primes = set([2])
    prime = 3
    number = 600851475143
    number = divideOut(number,2)
    while(number != 1):
        isPrime = True
        for p in primes:
            if prime%p == 0:
                isPrime = False
                prime += 2
                break
        if isPrime:
            number = divideOut(number,prime)
            primes.add(prime)
            prime += 2
    print prime-2

main()
