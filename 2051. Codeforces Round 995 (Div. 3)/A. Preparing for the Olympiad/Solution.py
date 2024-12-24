import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(maput())
    b = list(maput())
    ans = a[-1]
    for i in range(n-1):
        if a[i] > b[i+1]:
            ans += a[i] - b[i+1]
    printf(str(ans) + '\n')
