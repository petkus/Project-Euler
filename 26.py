# Finished
def findCycle(n):
    cycled = dict()
    div = 1
    count = 0
    while div / n != 1:
        count += 1
        div *= 10
        rem = div % n
        if rem in cycled.keys():
            return count - cycled[rem]
        cycled[rem] = count
        div = rem
    return 0
m = 0
ma = 0
for x in xrange(1, 1000):
    a = findCycle(x)
    if m < a:
        ma = x
        m = a
print ma
print m
