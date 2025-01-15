import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

from collections import defaultdict

for _ in range(t):
    n = int(input())
    seen = defaultdict(list)
    for i in range(n-1):
        u, v = maput()
        seen[u].append(v)
        seen[v].append(u)

    leafs = 0
    morethan1 = 0
    ones = 0

    for i in seen:
        if len(seen[i]) == 1:
            leafs += 1
        elif (p:=sum(1 for j in seen[i] if len(seen[j]) > 1)) != len(seen[i]):
            ones += p-1
        else:
            morethan1 += 1
    # print(val)
    # print(leafs, morethan1, ones)
    ans = leafs * (n-leafs) + morethan1 * ones
    printf(str(ans) + '\n')
