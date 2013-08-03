def divisor_sum(N):
	sum = 0
	for n in xrange(1, N):
		if N % n == 0:
			sum += n
	return sum


def is_abundant(N):
	return divisor_sum(N) > N


def solve_it():
	gabs = set()
	non_gabs_sum = 0
	for n in xrange(28123):
		if is_abundant(n):
			gabs.add(n)
		for g in iter(gabs):
			if n - g in gabs:
				break
		else:
			non_gabs_sum += n
	return non_gabs_sum


if __name__ == "__main__":
	print solve_it()
