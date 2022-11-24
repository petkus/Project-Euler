# Finished
import math
import scripts

def concatenate(p1,p2):
    return p1 * 10 ** math.ceil(math.log(p2,10)) + p2

primes = list(scripts.find_primes(10**4))

# Took close to a minute:
s = 10**8
for i0 in range(0,len(primes)):
    p0 = primes[i0]
    for i1 in range(i0+1, len(primes)):
        p1 = primes[i1]
        con = scripts.is_prime(concatenate(p1,p0)) and scripts.is_prime(concatenate(p0,p1)) 
        if con:
            for i2 in range(i1+1, len(primes)):
                p2 = primes[i2]
                con = all([scripts.is_prime(concatenate(p,p2)) and
                          scripts.is_prime(concatenate(p2,p)) for p in [p0,p1]])
                if con:
                    for i3 in range(i2+1, len(primes)):
                        p3 = primes[i3]
                        con = all([scripts.is_prime(concatenate(p,p3)) and
                                   scripts.is_prime(concatenate(p3,p)) for
                                   p in [p0,p1,p2]])
                        if con:
                            print(s)
                            print([p0,p1,p2,p3])
                            for i4 in range(i3+1, len(primes)):
                                p4 = primes[i4]
                                con = all([scripts.is_prime(concatenate(p,p4))
                                           and
                                           scripts.is_prime(concatenate(p4,p))
                                           for p in [p0,p1,p2,p3]])
                                if con:
                                    print([p0,p1,p2,p3,p4])
                                    s = min([s, p0+p1+p2+p3+p4])
print(s)

