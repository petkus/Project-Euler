import clipboard
for c in xrange(400, 1000):
    a = 1
    b = 2
    for a in xrange(1, c):
        b = 1000 - a - c
        if a ** 2 + b ** 2 == c ** 2 and b > 0:
            print "here"
            print a
            print b
            print c
            clipboard.copy(str(a * b * c))
