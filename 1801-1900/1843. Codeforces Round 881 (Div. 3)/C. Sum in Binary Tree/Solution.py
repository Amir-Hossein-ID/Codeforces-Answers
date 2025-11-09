import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    ans = 1
    while n != 1:
        ans += n
        n //= 2
    print(ans)
