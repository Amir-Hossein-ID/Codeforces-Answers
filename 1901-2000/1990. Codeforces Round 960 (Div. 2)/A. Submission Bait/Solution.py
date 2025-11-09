import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

from collections import Counter

for i in range(t):
    n = int(input())
    a = list(maput())
    aa = Counter(a)
    for i in aa:
        if aa[i] % 2:
            print("YES\n")
            break
    else:
        print('NO\n')
