import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n = int(input())
    if n == 3:
        print(-1)
        continue
    print(*range(3,n+1), end=' 2 1\n')
