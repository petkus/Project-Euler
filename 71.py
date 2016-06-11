def findClosest(n):
    for x in xrange(1, n):
        if (float(x) / float(n) > 3.0 / 7.0) and n % 7 != 0:
            return [3.0 / 7.0 - (float(x - 1) / float(n)), n, x]
    return [1, 1]

min = [1, 1]
for k in xrange(8, 1000000):
    cur = findClosest(k)
    if min[0] > cur[0]:
        min = cur
        print cur
print min
