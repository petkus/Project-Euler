a = [
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

def most(lat, lon):
    if lon == 14:
        return a[lon][lat]
    return a[lon][lat] + max(most(lat, lon + 1), most(lat + 1, lon + 1))
print most(0,0)

"""
Wrong
def searching(index,checked):
    lat = index[0]
    lon = index[1]
    if lon == 14:
        return a[lon][lat]
    if index in checked:
        return checked[index]
    checked[index] = a[lon][lat]
    l = a[lon + 1][lat]
    r = a[lon + 1][lat + 1]
    if l > r:
        return searching([lat, lon + 1], checked) + l
    elif l < r:
        return searching([lat + 1, lon + 1], checked) + r
    else:
        return max(searching([lat + 1, lon + 1], checked) + r, searching([lat, lon + 1], checked) + l)
m = 0
checked = dict()
for k in xrange(len(a)):
    for j in xrange(len(a[k])):
        n = searching([j,k], checked)
        print n
        m = max(m, n)
print m
"""
