import math
bot = math.floor(math.sqrt(1020304050607080900))
top = math.ceil(math.sqrt(1929394959697989990))
import re
pat = re.compile("^1.2.3.4.5.6.7.8.9.0$")
for x in xrange(int(bot), int(top)):
	if pat.match(str(x * x)):
		print x
		print x * x
		break
        print x
print x
