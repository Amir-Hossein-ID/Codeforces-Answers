import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n,m,k = maput()
    ms = maput()
    ks = maput()
    if n > k+1:
        printf("0" * m + "\n")
    elif n == k:
        printf("1" * m + "\n")
    else:
        ans = set(range(1,n+1)) - set(ks)
        for i in ms:
            if i in ans:
                printf("1")
            else:
                printf("0")
        printf("\n")
