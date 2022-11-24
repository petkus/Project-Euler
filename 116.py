# Finished
def r(x):
    r1 = 1
    r2 = 2
    for i in xrange(3, x + 1):
        temp = r2
        r2 = r2 + r1
        r1 = temp
    return r2 - 1

def g(x):
    g1 = 1
    g2 = 1
    g3 = 2
    for i in xrange(4, x + 1):
        temp = g3
        g3 = g1 + g3
        g1 = g2
        g2 = temp
    return g3 - 1

def b(x):
    b1 = 1
    b2 = 1
    b3 = 1
    b4 = 2
    for i in xrange(5, x + 1):
        temp = b4
        b4 = b1 + b4
        b1 = b2
        b2 = b3
        b3 = temp
    return b4 - 1
print r(50)
print g(50)
print b(50)
print r(50) + g(50) + b(50)
