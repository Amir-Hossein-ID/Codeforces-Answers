import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    a = list(maput())
    min_ = float('inf')
    for i in range(11):
        min_ = min(min_, sum(abs(j-i) for j in a))
    printf(min_)
