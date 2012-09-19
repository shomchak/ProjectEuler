# We can use the fact that two adjacent integers are coprime, therefore a triangle
# number cannot be a perfect power.

import math,time

start = time.time()

def numOfDivisors(n):
	divisors = 0
	allDivisors = []
	for d in range(1,int(math.sqrt(n+1))):
		if (n%d == 0):
			divisors += 2
			allDivisors.append(d)
                        allDivisors.append(n/d)
	return allDivisors

def triangleDivisors(M,N):
	allPairs = []
	for m in M:
		for n in N:
			allPairs.append(m*n)
        count = 0
	for a in allPairs:
		if(a%2 == 0):
                        count += 1
	return count

def findAllDivisors(N):
	Mdivisors = numOfDivisors(N)
	Ndivisors = numOfDivisors(N+1)
	divisors = triangleDivisors(Mdivisors,Ndivisors)
	return divisors

def main():
        n=1
	complete = False
	while(not complete):
		D = findAllDivisors(n)
                #print "D(T) =", D
		if(D > 500):
			complete = True
			print "Triangle number is", n*(n+1)/2
		else:
			n += 1	

main()
print time.time()-start
