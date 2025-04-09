import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

def dif(a):
    for i in range(len(a)-1):
        a[i] = a[i+1] - a[i]
    return a[:-1]

for _ in range(t):
    n = int(input())
    a = list(maput())

    ans = sum(a)
    while len(a) > 1:
        ans =max(ans, a[-1] - a[0], a[0] - a[-1])
        a = dif(a)

    printf(str(ans) + '\n')
