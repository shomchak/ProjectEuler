dataFile = open('e8input.txt')
data = dataFile.readline()

max = 0
for n in range(len(data)-4):
	product = 1
	for i in range(5):
		product = product*(ord(data[n+i])-48)
	if (product > max):
		max = product

print max
