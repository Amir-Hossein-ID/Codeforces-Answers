import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n,k = maput()
    d = n//k
    ans = []
    for i in range(n):
        ans.append(input())
    for i in range(d):
        for j in range(d):
            print(str(ans[i*k][j*k]))
        print('\n')
