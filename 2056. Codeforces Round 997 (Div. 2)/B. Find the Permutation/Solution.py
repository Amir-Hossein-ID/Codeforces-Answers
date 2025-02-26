import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n= int(input())
    table = [input() for i in range(n)]
    ans = [0] * n
    canchoose = list(range(1, n+1))
    for i,j in enumerate(table):
        ss = j.count('1', i+1)
        ss2 = j.count('0', 0, i)
        ans[ss+ss2] = i+1
    
    for i in range(n-1, -1, -1):
        printf(str(ans[i]) + ' ')
