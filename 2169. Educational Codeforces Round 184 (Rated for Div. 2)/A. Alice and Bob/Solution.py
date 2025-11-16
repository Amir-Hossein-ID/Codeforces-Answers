import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for i in range(t):
    n,a = maput()
    v = list(maput())
    m = l = 0
    for i in v:
        if i > a:
            m += 1
        elif i < a:
            l += 1
    
    print([a+1, a-1][m < l])
