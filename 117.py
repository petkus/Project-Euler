# Finished
import clipboard
def f(x):
    a1 = 1
    a2 = 2
    a3 = 4
    a4 = 8
    for i in xrange(5, x + 1):
        temp = a4
        a4 = a1 + a2 + a3 + a4
        a1 = a2
        a2 = a3
        a3 = temp
    return a4

print f(5)
print f(50)
clipboard.copy(str(f(50)))

