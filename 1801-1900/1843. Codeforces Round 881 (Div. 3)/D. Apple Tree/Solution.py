import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

from collections import defaultdict

t = int(input())

def count_leaves():
    to_see = [(1,0)]
    to_add = []
    while to_see:
        n, p = to_see.pop()
        if c[n] == [p]:
            leaves[n] = 1
        for i in c[n]:
            if i != p:
                to_see.append((i, n))
                to_add.append((n, i))
    while to_add:
        p, n = to_add.pop()
        leaves[p] += leaves[n]

for i in range(t):
    n = int(input())
    c = defaultdict(list)
    leaves = defaultdict(int)
    for i in range(n-1):
        u, v = maput()
        c[u].append(v)
        c[v].append(u)
    count_leaves()
    q = int(input())
    for i in range(q):
        x, y = maput()
        print(leaves[x] * leaves[y])
