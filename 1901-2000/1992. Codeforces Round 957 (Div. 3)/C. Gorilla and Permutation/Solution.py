import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n,m,k = maput()
    for i in range(n, k-1, -1):
        print(str(i) + ' ')
    for i in range(m+1, k):
        print(str(i) + ' ')
    for i in range(1, m+1):
        print(str(i) + ' ')
    print('\n')
