import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

from collections import Counter
import bisect

for _ in range(t):
    n = int(input())
    cant = Counter()
    a = []
    for i in range(n):
        b,c = maput()
        a.append((b,c))
        if b==c:
            cant[b] += 1
    c = sorted(cant)
    cc = len(c)
    if not c:
        printf(n*'1')
        printf('\n')
        continue
    for i,j in a:
        if i == j:
            if cant[i] > 1:
                printf('0')
            else:
                printf('1')
            continue
        # 4 5
        aa = bisect.bisect_right(c, j)
        bb = bisect.bisect_right(c, i)
        # print(aa, bb, 'asd')
        if (aa == bb) or (aa - bb + 1 < j - i + 1) or (c[bb-1] != i):
            printf('1')
        else:
            printf('0')
    printf('\n')
