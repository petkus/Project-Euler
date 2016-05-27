names = open("p022_names.txt", "r")
blah = names.read()
array = eval('[' + blah + ']')
array = sorted(array)
x = 0
for i in xrange(len(array)):
    valu = 0
    for c in array[i]:
        valu += ord(c) - ord('A') + 1
    x +=  valu * (i + 1)
print x




