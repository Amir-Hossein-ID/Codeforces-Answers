import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    b = sorted(maput())
    cur = n-1
    ind = 0
    while ind != n*(n-1)//2:
        print(b[ind], end = ' ')
        ind += cur
        cur -= 1
    print(b[ind-1])
