import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

from math import log

t = int(input())

for i in range(t):
    n,k = maput()
    ans = 0
    if k == 1:
        print(str(n) + '\n')
        continue
    while n >= k:
        s = int(log(n, k))
        ans += 1
        n -= k ** s
    print(str(ans + n) + '\n')
