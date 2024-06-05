import math
import time
from collections import Counter
FIXED_RANDOM = int(time.time()*100000)
def mk(k):
    k+=FIXED_RANDOM
    k+=0x9e3779b97f4a7c15
    k=(k^(k>>30))*0xbf58476d1ce4e5b9
    k=(k^(k>>27))*0x94d049bb133111eb 
    return k^(k>>31)
t = int(input())
start = time.time()
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    b = [int(x) for x in input().split(" ")]
    z = int(input())
    d = [int(x) for x in input().split(" ")]
    r = []
    for i in range(n):
        if b[i]!=a[i]:
            r.append(b[i])
    cr = Counter(r)
    cd = Counter(d)
    if cd>=cr and d[z-1] in b:
        print("YES")
    else:
        print("NO")
end = time.time()
print("{}ms".format(int((end-start)*1000)))