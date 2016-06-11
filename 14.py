dic = {1: 1}

def collatz(n, dic):
    if n in dic:
        return dic[n]
    if n % 2 == 0:
        return 1 + collatz(n/2, dic)
    else:
        return 1 + collatz(3 * n + 1, dic)
ma = 1
most = 1
for x in xrange(1,1000000):
    a = collatz(x, dic)
    dic[x] = a
    print a
    if ma < a:
        ma = a
        most = x
print most

