t = int(input())

from math import log2

for i in range(t):
    l, r = [int(i) for i in input().split()]
    print(int(log2(r)))
