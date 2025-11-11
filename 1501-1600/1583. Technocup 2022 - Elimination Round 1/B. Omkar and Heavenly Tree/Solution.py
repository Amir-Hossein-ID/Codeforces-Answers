import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for i in range(t):
    n, m = maput()
    d = [1] * (n+1)
    for i in range(m):
        a,b,c = maput()
        d[b] = 0
    root = d.index(1, 1)
    i = 1
    while i <= n:
        if i != root:
            print(root, i)
        i += 1
