# A faster solution. We know three things at the outset:
# 
# a<b<c  
# a + b + c = 1000
# a^2 + b^2 = c^2.
#
# We can combine these equations into 
#
# b = 1000(500-a)/(1000-a).
#
# We can also glean that a cannot exceed 332, because if it did
# a+b+c must necessarily exceed 1000. 

import math, time

s=time.time()
a = 332
while(a>0):
    b = 1000*(500-a)/(1000-a)
    if(b*(1000-a) + 1000*a == 500000):
        print a*b*(1000-a-b)
        print time.time()-s
        break
    a -= 1

