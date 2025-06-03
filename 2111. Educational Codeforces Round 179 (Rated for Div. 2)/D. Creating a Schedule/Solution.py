import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n, m = maput()
    a = list(maput())
    a.sort()
    cur = 0
    for i in range(0,n,2):
        f = a[cur]
        l = a[m-cur-1]
        cur += 1
        print(f,l,f,l,f,l)
        if i < n-1:
            print(l,f,l,f,l,f)
