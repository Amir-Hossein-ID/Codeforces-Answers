import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

from collections import defaultdict

# to prevent the hack
import random
RANDOM = random.randrange((1 << 31) - 1)
class newDefaultDict(defaultdict):
    def __setitem__(self, __k, __v):
        return super().__setitem__(__k ^ RANDOM, __v)

    def __delitem__(self, __k):
        return super().__delitem__(__k ^ RANDOM)

    def __getitem__(self, __k):
        return super().__getitem__(__k ^ RANDOM)

    def __contains__(self, __o: object) -> bool:
        return super().__contains__(__o ^ RANDOM)

def solve():
    _, k = maput()
    c = newDefaultDict(int)
    for i in maput():
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
