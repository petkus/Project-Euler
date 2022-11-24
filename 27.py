# Finished
import primes

checkb = primes.findPrimes(1000)
prime = primes.findPrimes(100000)
m = 0
for b in checkb:
    for a in xrange(-1000, 1000):
        n = 0
        while n ** 2 + a * n + b in prime:
            n += 1
        if m < n:
            m = n
            ma = [a, b]
print m
print ma
print ma[0] * ma[1]
