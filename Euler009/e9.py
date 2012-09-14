import math,time

def isPerfectSquare(n):
	floatVal = math.sqrt(n)
	if(floatVal%1 == 0):
		return True
	else:
		return False

def isTriplet(a,b,c):
	if((a*a + b*b) == (c*c)):
		return True
	else:
		return False

s = time.time()
c = 500
condition = True
while(condition):
	for b in range(c/2):
		b = b + 1
		a = 1000 - c - b
		if(isTriplet(a,b,c)):
			result = [a,b,c,a*b*c]
			print result
			condition = False
			break
		else:
			continue
	c = c - 1
	if (c <= 10):
		result = "fail"
		print result
		break
	
print time.time()-s
		


