import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

from collections import defaultdict

def solve():
    _, k = maput()
    c = defaultdict(int)
    a = sorted(maput())
    for i in a:
        c[i] += 1
    ans = len(c)
    for i in sorted(c.values()):
        if i > k:
            printf(str(max(ans, 1)) + '\n')
            return
        k -= i
        ans -= 1
    printf('1\n')

for _ in range(int(input())):
    solve()
