import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n,l,r = maput()
    a = list(maput())
    b = sorted(a[l-1:])
    c = sorted(a[:r])
    ans = min(sum(b[:r-l+1]), sum(c[:r-l+1]))
    printf(str(ans) + '\n')
