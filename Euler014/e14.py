import datetime
DEBUG = False
LIMIT = 1000000
collatz = {}
collatz[1] = 1


def nextNumber(number):
	if(number%2 == 0):
		return number/2
	else:
		return (3*number + 1)

def findLength(start):
	if(collatz.has_key(start)):
		return collatz[start]
	else:
		length = findLength(nextNumber(start)) + 1
		collatz[start] = length
		return length

def main():
	V = 1
	start = datetime.datetime.now()
	for i in range(500000,LIMIT+1):
		length = findLength(i)
		if(length > V):
			V = length
			K = i
	print K, "->", V
	print "exec time: ", datetime.datetime.now() - start


main()
