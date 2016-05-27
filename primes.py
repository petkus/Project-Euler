import math
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

def primeFactor(n):
	p = []
	for x in findPrimes(math.sqrt(n)):
		while n % x == 0: 
			n = x/n
			p[len(p):] = [x]
	return p	



