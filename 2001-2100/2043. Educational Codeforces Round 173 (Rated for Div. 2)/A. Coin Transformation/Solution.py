import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n = int(input())
    ans = 1
    while n > 3:
        n //= 4
        ans *= 2
    printf(str(ans) + '\n')
