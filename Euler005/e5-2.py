# A faster approach that explicitly makes use of the notion that prime
# factorizations are unique and that for a prime p < N, the product
# p^a (where a in an integer such that p^(a+1) is the least exponent 
# of p exceeding N) will be a factor in at least one factorization
# of a positive integer n <= N. 
#
# The algorithm steps through the primes below the given limit and
# calculates the exponent a (described above). Then you simply multiply
# all the primes ^ their respective a's together to get the number.
#

import math
import sieveOfEratosthenes

limit = 20
primes = sieveOfEratosthenes.getPrimes(limit)
product = 1
for p in primes:
    count = 1
    while(math.pow(p,count) <= limit):
        product *= p
        count += 1
print product
