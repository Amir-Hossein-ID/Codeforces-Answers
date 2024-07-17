import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

import math

for i in range(t):
    n,k = maput()
    printf(math.ceil((n-1)/(k-1)))
