import math,time

start = time.time()

total = 0
for digit in str(2**1000):
    total += int(digit)
print total

print time.time()-start
