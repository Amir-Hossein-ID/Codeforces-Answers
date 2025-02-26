import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n = int(input())
    printf('1 ')
    if n % 2:
        for i in range(1, n//2+1):
            printf(str(i) + ' ')
        for i in range(1, n//2+1):
            printf(str(i) + ' ')
    else:
        for i in range(1, n//2+1):
            printf(str(i) + ' ')
        for i in range(1, n//2):
            printf(str(i) + ' ')
    printf('\n')
