import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    a = list(maput())
    for i in range(5):
        a.sort()
        a[0] += 1
    printf(a[0] * a[1] * a[2])
