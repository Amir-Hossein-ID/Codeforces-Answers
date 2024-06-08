import sys

import bisect
from decimal import Decimal # the division gave incorrect results with normal float

input = sys.stdin.readline
print = sys.stdout.write

t = int(input())

for _ in range(t):
    n,k,q = map(int, input().strip().split())
    a = [0] + [int(i) for i in input().strip().split()]
    b = [0] + [int(i) for i in input().strip().split()]
    d = [int(input()) for i in range(q)]
    ans = ''
    for i in d:
        if i == n:
            print(str(b[-1]) + ' ')
            continue
        elif i == 0:
            print('0 ')
            continue
        where = bisect.bisect_right(a, i)
        print(str(int((i - a[where - 1]) * (b[where] - b[where-1]) / Decimal(a[where] - a[where - 1]) + b[where-1])) + ' ')
    print('\n')
