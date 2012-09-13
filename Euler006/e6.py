limit = 100 
sum1 = reduce(lambda x,y: x+y, map(lambda x: x*x, range(1,limit+1)))
sum2 = limit*(limit+1)/2
print sum1-sum2**2