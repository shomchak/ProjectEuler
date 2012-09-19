def readInGrid(filename):
	grid = open(filename)
	lines = []
	for line in grid:
		lines.append(line)
	grid.close()
	grid = []
	for m in lines:
		row = []
		j = 1
		tens = 0
		ones = 0
		for n in m:
			if((ord(n) != 32) and (ord(n) != 10)):
				if(j == 1):
					tens = (ord(n) - 48)
					j = 2
				elif(j == 2):
					ones = (ord(n) - 48)
					currentNumber = (10*tens + ones)
					row.append(currentNumber)
					j = 1
		grid.append(row)
	return grid

def horizontals(grid,n):
	numRows = len(grid)
	numCols = len(grid[0])
	productsPerRow = (numCols - n + 1)
	products = []
	for row in grid:
		for i in range(productsPerRow):
			product = 1
			for j in range(4):
				product = product * row[i+j]
			products.append(product)
	return products

def verticals(grid,n):
	newGrid = []
	for i in range(len(grid[0])):
		newGrid.append([])
	for row in grid:
		for i in range(len(row)):
			newGrid[i].append(row[i])
	return horizontals(newGrid,n)

def diagonals(grid,n):
	numRows = len(grid)
	numCols = len(grid[0])
	x = (numCols - n + 1)
	y = (numRows - n + 1)
	products = []
	for i in range(y):
		for j in range(x):
			left = 1
			right = 1
			for d in range(4):
				left = left*grid[i+d][j+d]
			products.append(left)
			for d in range(4):
				right = right*grid[y-1-i-d][j+d]
			products.append(right)
	return products


def main():
	grid = readInGrid('grid.txt')
	horz = max(horizontals(grid,4))
	vert = max(verticals(grid,4))
	diag = max(diagonals(grid,4))
	return max(horz,vert,diag)

print main()



