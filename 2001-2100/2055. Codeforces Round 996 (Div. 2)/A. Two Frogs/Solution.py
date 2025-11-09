import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n,a,b = maput()
    if abs(a-b) % 2:
        print('NO')
    else:
        print('YES')
