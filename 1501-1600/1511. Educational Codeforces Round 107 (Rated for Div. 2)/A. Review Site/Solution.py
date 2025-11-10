import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    ans = 0
    for i in maput():
        if i != 2:
            ans += 1
    print(ans)
