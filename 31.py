a = [1,2,5,10,20,50,100, 200]
ans = []
good = []
def check(n):
    if n == 0:
        good[len(a):] = ans
        ans = []
    elif n < 0:
        ans = []
        x = 0
    else: 
        for k in a:
            ans += [k]
            check(n - k)

check(200)
print good
