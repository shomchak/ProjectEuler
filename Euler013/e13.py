import math,time

start = time.time()

def readInGrid(filename):
	grid = open(filename)
	lines = grid.readlines()
	grid.close()
	Numbers = []
        for line in lines[0:-1]:
                Number = int(line[0:-1]) 
		Numbers.append(Number)
	return Numbers

def sumTheNumbers(Numbers):
	sum = 0L
	for Number in Numbers:
		sum = sum + Number
	return sum

def main(filename):
        print str(sumTheNumbers(readInGrid(filename)))[0:10]

main('grid.txt')
print time.time() - start
