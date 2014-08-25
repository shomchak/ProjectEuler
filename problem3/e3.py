
def solve(number=600851475143):
    '''
    Starting with 2, find new primes and divide the number until it is 1.
    '''
    primes = set((2,))
    prime_candidate = 3
    current = divide_out(number, 2)

    while current != 1:
        is_prime = True
        for p in primes:
            if prime_candidate % p == 0:
                is_prime = False
                prime_candidate += 2
                break
        if is_prime:
            current = divide_out(current, prime_candidate)
            primes.add(prime_candidate)
            prime_candidate += 2

    return prime_candidate - 2


def divide_out(n, p):
    return divide_out(n / p, p) if n % p == 0 else n
