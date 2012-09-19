# the solution is 40 choose 20.

# just implement the factorial function
total = 1
for i in range(40,0,-1):
	if(i>20):
		total = total*i
	else:
		total = total/i
print total
