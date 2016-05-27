x = 1
y = 1
index = 2
while len(str(y)) < 1000:
    cur = y
    y += x
    x = cur
    index += 1
print index
