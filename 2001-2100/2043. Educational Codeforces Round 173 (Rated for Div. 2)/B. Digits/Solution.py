import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())


for _ in range(t):
    n,d = maput()
    printf("1 ")
    if d % 3 == 0 or n >= 3:
        printf("3 ")
    if d == 5:
        printf("5 ")
    if n >= 3 or d == 7:
        printf("7 ")
    if d == 9 or (n >=3 and d % 3 == 0) or n >= 6:
        printf("9 ")
    printf("\n")
