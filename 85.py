def f(n,m):
	return ((n*m)*(n*m)+n*m)/2
def g(n):
	m = 1
	while f(n,m) < 2000000:
		m+=1
	return m
arr = []
for n in xrange(1,100):
	arr.append([n,g(n)])
	arr.append([n,g(n) - 1])
differences = [abs(2000000 - f(x,y)) for x, y for a in arr]
print differences
print min(differences)
print arr[0]
print arr[1]
print sum(arr[0])
