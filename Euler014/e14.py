import time

start = time.time()

def nextNumber(number):
	if(number%2 == 0):
		return number/2
	else:
		return (3*number + 1)

def collatzSequence():
	starter = {}
	starter[1] = 1
	sequenceLength = [1]
	limit = 1000000
	for n in range(2,limit+1):
		starterCache = []
		m = n
		while(m != 1):
			if(starter.has_key(m)):
				break
			else:
				starterCache.append(m)
				m = nextNumber(m)
		if(len(starterCache) > 0):
			length = sequenceLength[starter[m]]
			for i in range(len(starterCache)):
				length = length + 1		
				starter.append(starterCache[-(i+1)])
				# print "new n: ", starter[-1]
				sequenceLength.append(length)
				# print "new length: ", sequenceLength[-1]

		else:
			length = sequenceLength[starter.index(m)] + 1
			starter.append(n)
			# print "new n: ", n
			sequenceLength.append(length)
			# print "new length: ", length
	return [starter, sequenceLength]

def maxOfSequence(pairs):
	return pairs[0][pairs[1].index(max(pairs[1]))]

result = maxOfSequence(collatzSequence())
print "max starter is ", result
print time.time() - start
