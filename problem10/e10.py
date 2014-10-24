from PrimeSieve import primeGenerator
import time

start = time.time()
limit = 2000000
print reduce(lambda x,y:x+y,primeGenerator(limit)), "\ntook", time.time()-start,"s"
