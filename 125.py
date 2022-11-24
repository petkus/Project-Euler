import numpy as np

def isPalendrom(n):
    s = str(n)
    for i in range(int(len(s)/2)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

def find_palendromic_sums(n):
    S = set()
    for i in range(1,int(np.sqrt(n))):
        j = i + 1
        s = i**2 + j**2
        while s < n:
            if isPalendrom(s):
                S.add(s)
            j += 1
            s = sum(k**2 for k in range(i,j+1))
    return S
S = find_palendromic_sums(10**8)  
print(S)
print(sum(s for s in S))


