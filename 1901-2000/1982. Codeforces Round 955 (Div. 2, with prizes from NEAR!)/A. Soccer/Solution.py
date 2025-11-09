import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    a,b = maput()
    c,d = maput()

    if (a >= b and c >= d) or (b >= a and d >= c):
        print('YES\n')
    else:
        print('NO\n')
