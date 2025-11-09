import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())
for _ in range(t):
    l,r = maput()
    ans = r - l
    if ans == 0 and l == 1:
        ans += 1
    print(ans)
