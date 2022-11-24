# Finished
import math
i = 10
sum = 0
while math.factorial(9) * math.log(i) > i:
    s = 0
    for d in str(i):
        s += math.factorial(int(d))
    if i == s:
        print str(i) + "equals" + str(s)
        sum += i
    i += 1
print "answer: " + str(sum)
