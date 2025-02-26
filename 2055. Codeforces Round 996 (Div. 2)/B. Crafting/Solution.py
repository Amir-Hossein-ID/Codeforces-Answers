import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n= int(input())
    a = list(maput())
    b = list(maput())
    want = 0
    wanted = False
    can = float('inf')
    for i,j in zip(a,b):
        if i < j:
            if wanted:
                printf('NO\n')
                break
            want = j - i
            wanted = True
        else:
            can = min(can, i - j)
    else:
        if (wanted and can >= want) or not wanted:
            printf("YES\n")
        else:
            printf('NO\n')
