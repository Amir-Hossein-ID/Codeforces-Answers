import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

from collections import defaultdict

for i in range(t):
    n = int(input())
    a = list(maput())
    s = 0
    b = {}
    bb = defaultdict(int)
    madmax = 0
    for i in a:
        s += i
        if i in b:
            b[i] += 1
            if i > madmax:
                madmax = i
        else:
            b[i] = 1
        if madmax:
            bb[madmax] += 1
    # the array becomes sorted after one iteration, so dictionary bb has the keys in order
    b = bb
    bb = defaultdict(int)
    while b:
        cur = 0
        for i in b:
            s += b[i] * i
            bb[cur] += 1
            if b[i] > 1:
                bb[i] += b[i] - 1
                cur = i
        del bb[0]
        b = bb
        bb = defaultdict(int)
    print(str(s) + '\n')
