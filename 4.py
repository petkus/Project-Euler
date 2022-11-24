# Finished
p = []
for x in xrange(100,999): 
	for y in xrange(100,x):
		if str(x*y) == str(x*y)[::-1]:
			p[len(p):] = [x*y]
print max(p)

