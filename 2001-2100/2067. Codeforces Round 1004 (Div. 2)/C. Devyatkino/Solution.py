import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    m = int(input())
    cur = 9
    ans = 10
    has7 = lambda x: '7' in str(x)
    while cur < 9999999999:
        n = m
        anss = 0
        while not has7(n):
            n += cur
            anss += 1
        ans = min(ans, anss)
        cur = 9 + cur*10

    print(ans)
