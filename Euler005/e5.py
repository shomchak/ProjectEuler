# A straight forward prime factorization approach. First find the prime 
# factorizations of each number 1-20. Then take the union of all the 
# factorizations and then multiply out the union to get the number.

import math
import sieveOfEratosthenes

def divideOut(N,p,times):
    if N%p == 0:
        times += 1
        return divideOut(N/p,p,times)
    else:
        return times

def factors(n,primes):
    facts = {}
    for p in primes:
        facts[p] = divideOut(n,p,0)
    return facts
    
def main():
    num = 20
    primes = sieveOfEratosthenes.getPrimes(num)
    primefactors = map(factors,range(2,num+1),[primes]*(num-1))
    minfactors = {}
    for p in primes:
        minfactors[p] = 0
    for factor in primefactors:
        for key in factor.keys():
            if factor[key] > minfactors[key]:
                minfactors[key] = factor[key]
    product = 1
    for prime in minfactors.keys():
        product *= math.pow(prime,minfactors[prime])
    print int(product)

main()