x = 3
primes = [2]
while len(primes) < 10001:
	isprime = True
	for prime in primes:
		if x % prime == 0:
			isprime = False	
			break
	if isprime:
		primes += [x]
	x += 1
print primes[-1]
