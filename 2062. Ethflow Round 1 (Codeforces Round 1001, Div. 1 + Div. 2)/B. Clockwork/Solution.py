import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(maput())
    for i,j in enumerate(a):
        if j <= max(i*2, (n-i-1)*2):
            printf("NO\n")
            break
    else:
        printf('YES\n')
