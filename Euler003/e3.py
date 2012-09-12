# Starting with our list of primes (currently [2,3]), the algorithm will go sequentially 
# through the list and try dividing theNumber by each element of the list. If an element divides evenly, 
# that number is added to our list of prime factors, and the algorithm keeps dividing by that element until
# it no longer divides, at which point it moves on to the next highest prime in out list (if it does not 
# divide evenly, the algorithm also moves on the to the next prime). If we are at the end of the list, we 
# call the findNextPrime function to add the next highest prime to our list of primes, and the algorithm 
# continues. Each time theNumber is successfully divided, we redefine theNumber as the quotient of that division,
# so we're not always dividing that huge starting number. We know we are done when theNumber equals 1, because 
# that means we have divided it by every prime factor as many times as possible.


def isPrime(n,primes):  ## tests the primality of a number "n"...
	for p in primes:	## ...given a list of currently known primes
		if(n%p == 0):
			return False
	return True

def findNextPrime(newPrime,primes):   ## finds the next prime given a starting guess "n" and...
	if(isPrime(newPrime, primes)):	  ## ...a list of currently known primes
		return newPrime
	else:
		return findNextPrime((newPrime+2),primes) ## recursion (the function calls itself)

def main():
	theNumber = 600851475143 
	primes = [2,3] 
	primeFactors = [] 
	currentPrimeIndex = 0 
	lastPrime = 1 
	complete = False 
	while(not complete):
		if(theNumber%primes[currentPrimeIndex] == 0):
			theNumber = theNumber/primes[currentPrimeIndex]
			if(primes[currentPrimeIndex] != lastPrime):
				primeFactors.append(primes[currentPrimeIndex])
				lastPrime = primes[currentPrimeIndex]
		else:
			currentPrimeIndex += 1
			if(len(primes) <= currentPrimeIndex):
				primes.append(findNextPrime(primes[-1]+2,primes))
			if(theNumber == 1):
				print "The prime factors are", primeFactors
				print "The largest prime factor is", lastPrime
				complete = True

main() 



