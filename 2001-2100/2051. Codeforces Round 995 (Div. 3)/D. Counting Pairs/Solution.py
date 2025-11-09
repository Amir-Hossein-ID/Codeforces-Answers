import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

import bisect

for _ in range(t):
    n,x,y = maput()
    ns = list(maput())
    ns.sort()
    s = sum(ns)
    ans = 0
    for i,k in enumerate(ns):
        ss = s - k
        aa = bisect.bisect_right(ns, ss - x)
        bb = bisect.bisect_left(ns, ss - y)
        # print(aa, bb, k)
        if i > bb and i < aa:
            ans += (aa - bb - 1)
        else:
            ans += (aa - bb)
    printf(str(ans // 2) + '\n')
