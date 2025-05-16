import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())


for i in range(t):
    n,m,p,q = maput()
    if n % p != 0:
        print('YES')
    elif m == q * n//p:
        print('YES')
    else:
        print('NO')
