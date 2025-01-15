import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(maput())
    flag = False
    for i in range(n-1):
        b = sorted((a[i], a[i+1]))
        if a[i] == a[i+1] or 2 * b[0] > b[1]:
            flag = True
            break
    if flag:
        printf('YES\n')
    else:
        printf('NO\n')
