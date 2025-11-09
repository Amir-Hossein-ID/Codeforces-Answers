import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

from collections import Counter

t = int(input())

def get_mex():
    cur = 0
    for i in ns:
        if i == cur:
            cur += 1
        elif i > cur:
            break
    return cur

def do_op():
    mex = get_mex()
    count = Counter(ns)
    for i,j in enumerate(ns):
        if count[j] > 1:
            ns[i] = mex
        elif j > mex:
            ns[i] = mex

for _ in range(t):
    n, k = maput()
    ns = sorted(maput())
    
    do_op()
    if k == 1:
        print(sum(ns))
        continue
    do_op()
    if k % 2 == 0:
        print(sum(ns))
        continue
    do_op()
    print(sum(ns))
