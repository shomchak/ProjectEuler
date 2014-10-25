from PrimeSieve import primeGenerator


limit = 2000000
print reduce(lambda x,y:x+y,primeGenerator(limit))
