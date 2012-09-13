def getPrimes(limit):
	allPrimes = []
	allNums = {}
	allNums[1] = False
	for i in range(2,limit+1):
		allNums[i] = True
	currentPrime = 2
	condition = True
	while(condition):
		currentMax = int(limit/currentPrime)
		for i in range(2,currentMax+1):
			allNums[currentPrime*i] = False
		for i in range(currentPrime+1,limit+1):
			if(allNums[i] == True):
				currentPrime = i
				break
			elif(i == len(allNums)):
				condition = False
	for i in range(1, len(allNums)+1):
		if(allNums[i] == True):
			allPrimes.append(i)
	return allPrimes
