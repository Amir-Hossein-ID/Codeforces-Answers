import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n,m = maput()
    xs = m
    ys = m
    _,_ = maput()
    for i in range(n-1):
        a,b = maput()
        xs += a
        ys += b
    
    print(2*xs + 2*ys)
