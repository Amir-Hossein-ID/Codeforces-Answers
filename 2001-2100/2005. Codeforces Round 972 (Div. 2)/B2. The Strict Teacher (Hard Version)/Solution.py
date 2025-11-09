import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

from bisect import bisect_right

for i in range(t):
    n,m,q = maput()
    b = list(maput())
    b.sort()

    for i in maput():
        x = bisect_right(b, i)
        if x == 0:
            print(str(b[0] - 1))
        elif x == m:
            print(str(n - b[-1]))
        else:
            print(str((b[x] - b[x-1])//2))
        print('\n')
