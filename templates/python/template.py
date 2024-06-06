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

def solve(n):
    ret = 0
    return ret

def inputOutput():
    n = int(input())
    print(solve(n))

def main():
    t = int(input())
    for _ in range(t):
        inputOutput()
main()
