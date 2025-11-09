import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n,a,b,c = maput()
    d = a+b+c
    ans = n // d * 3
    n %= d
    if n > 0:
        n-=a
        ans += 1
    if n > 0:
        n-=b
        ans += 1
    if n > 0:
        n-=c
        ans += 1
    printf(str(ans) + '\n')
