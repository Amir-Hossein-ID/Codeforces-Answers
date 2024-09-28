import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n,m,q = maput()
    b = list(maput())
    for i in maput():
        if i > max(b):
            print(str(n-max(b)))
        elif i < min(b):
            print(str(min(b) - 1))
        else:
            print(str(abs(b[0]- b[1]) // 2))
        print('\n')
