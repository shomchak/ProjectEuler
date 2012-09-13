limit = 100 
sum1 = 0
sum2 = limit*(limit+1)/2
for n in range(1, limit+1):
	sum1 += n**2
print sum1-sum2**2