import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())


for i in range(t):
    n = int(input())
    ans = 0
    for i,j in zip(range(n, 0, -1), range(1, n + 1)):
        ans += abs(i-j)
    print(ans//2+1)
