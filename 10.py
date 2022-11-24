# Finished
def findPrimes(i):
	primes = [2]
	for x in xrange(2,i):
		isprime = True
		for prime in primes:
			if x % prime == 0:
				isprime = False	
				break
		if isprime:
			primes += [x]
	return primes
print sum(findPrimes(2000000))
