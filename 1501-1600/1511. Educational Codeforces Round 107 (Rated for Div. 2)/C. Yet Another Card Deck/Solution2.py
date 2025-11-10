import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

n, q = maput()
a = list(maput())
for t in maput():
    ans = a.index(t)
    printf(str(ans + 1) + ' ')
    a[:ans+1] = [t] + a[:ans]
printf('\n')
