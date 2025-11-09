import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    a = sorted(maput())
    print(sum([a[n-i-1] - a[i] for i in range(n//2)]))
