def max_product(numstr):
    maximum = 0
    for n in range(len(numstr)-4):
    	product = 1
    	for i in range(5):
    		product = product*(int(numstr[i+n]))
    	if product > maximum:
    		maximum = product
    return maximum


if __name__ == '__main__':
    with open('e8input.txt') as f:
        numstr = f.readline()

    print max_product(numstr)
