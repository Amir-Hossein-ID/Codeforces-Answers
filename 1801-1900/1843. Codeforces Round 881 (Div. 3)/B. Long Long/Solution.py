import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    s = 0
    ans = 0
    last = False
    for i in maput():
        if i < 0:
            last = True
        elif i > 0:
            if last:
                ans += 1
            last = False
        s += abs(i)
    if last:
        ans += 1
    print(s, ans)
