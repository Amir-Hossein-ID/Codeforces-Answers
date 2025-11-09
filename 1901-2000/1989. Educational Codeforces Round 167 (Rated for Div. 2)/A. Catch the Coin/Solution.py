import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    a,b = maput()
    if b < -1:
        print('NO\n')
    else:
        print('YES\n')
