import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    a = sorted(maput())
    printf(abs(a[0] - a[1]) + abs(a[2] - a[1]))
