import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    a = list(maput())
    b = sum(a)
    if b % 2==0 or any(b % i==0 for i in range(3, (b+1)//2, 2)):
        printf(str(n) + '\n')
        for i in range(n):
            printf(str(i+1) + ' ')
    else:
        didnt = True
        printf(str(n-1) + '\n')
        for i in range(n):
            if didnt and a[i] % 2:
                didnt = False
            else:
                printf(str(i+1) + ' ')
    printf('\n')
