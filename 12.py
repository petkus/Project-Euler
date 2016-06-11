import clipboard
import primes
import math

def div(n):
    if n % 2 == 0:
        n = n / 2
    factors = 1
    for x in primes.findPrimes(int(math.ceil(math.sqrt(n)) + 1)):
        count = 0
        while n % x == 0:
            count += 1
            n = n / x
        factors = factors * (count + 1)
    if factors == 1:
        factors = 2
    return factors
print div(17)
print div(12)
print div(32)

ldiv = 2
rdiv = 2
r = 3
l = 2
while (ldiv * rdiv) <= 500:
    l = r
    ldiv = rdiv
    r += 1
    rdiv = div(r)
    print ldiv + rdiv
    print str(l * r / 2)
print str(l * r / 2)

"""
failed attempt ^retry
def div(x):
    d = 0
    for i in xrange(x / 2):
        if x % (i + 1) == 0:
            d += 1
    return d

x = 1
n = 1
while div(x) <= 500:
    x += n
    n += 1
    print x
print x
"""
