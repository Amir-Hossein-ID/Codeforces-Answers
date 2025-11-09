import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

from collections import Counter

for i in range(t):
    n,q = maput()
    x = list(maput())
    qs = list(maput())
    mi = n - 1
    count = Counter()
    count[mi] = 1
    last = x[0]
    bef = 1
    af = n - 1
    for i in x[1:]:
        bet = i - last - 1
        count[af*bef] += bet
        af -= 1
        count[af*bef + mi] += 1
        bef += 1
        last = i
    for i in qs:
        print(str(count[i]) + ' ')
    print('\n')
