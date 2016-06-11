import math
import itertools
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
	for x in findPrimes(int(math.floor(math.sqrt(n)))):
		while n % x == 0: 
			n = n / x
			p += [x]
        p += [n]
	return p	

def permutations(array):
    out = []
    for n in xrange(1, 2 ** len(array)):
        n = bin(n)
        s = str(n)[2:]
        perm = []
        for x in xrange(len(s)):
            if s[x] == '1':
                perm += [array[len(s) - len(array) - x - 1]]
        out += [perm]
    return out

def factors(n):
    factors = primeFactor(n)
    a = set()
    p = permutations(factors)
    for perm in p:
        a.add(reduce(lambda z,y: z*y, perm))
    return len(a)
