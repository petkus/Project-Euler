import math
def findPrimes(i):
	primes = [2]
	for x in range(2,i):
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
	for x in findPrimes(10000):
		while n % x == 0: 
			n = n/x
			p += [x]
	return p	

print max(primeFactor(600851475143))
