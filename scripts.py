import math

# Returns whether the given number n is prime
def is_prime(n):
    for i in range(2, math.floor(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

# Returns the list of primes less than given integer n
def find_primes(n):
    primes = set(range(2,n))
    for k in range(2,int(n/2)):
        s = 2 * k
        while s < n:
            if s in primes:
                primes.remove(s)
            s += k
    return primes

# Returns a dictionary of the form {prime factor : multiplicity} for a given
# integer n
def prime_factor(n):
    f = {}
    for p in find_primes(int(math.floor(math.sqrt(n)))):
        while n % p == 0: 
            n = n / p
            p[x] += 1
    return p

# Returns the powerset of a given set S
def powerset(S):
    P = set([])
    s = S.pop()
    for D in powerset(S):
        P.add(D)
        W = set(D)
        W.add(s)
        P.add(frozenset(W))
    S.add(s)
    return P
