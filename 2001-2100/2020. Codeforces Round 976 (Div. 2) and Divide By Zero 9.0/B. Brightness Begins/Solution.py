import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

from math import sqrt

for i in range(t):
    k = int(input())
    i = int(sqrt(k))
    while i ** 2 - i < k:
        i += 1
    t = (i-1) ** 2
    ans = t + k - (t - i + 1)
    print(str(ans) + '\n')
