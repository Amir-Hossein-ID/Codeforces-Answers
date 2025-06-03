import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for i in range(t):
    x=  int(input())
    a = [0,0,0]
    cur = 0
    ans = 0
    while a[1] != x:
        a.sort()
        a[0] = min(a[1]*2 + 1, x)
        ans += 1
    print(ans)
