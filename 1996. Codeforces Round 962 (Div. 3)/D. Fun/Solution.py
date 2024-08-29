import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n, x = maput()
    ans = 0
    for a in range(1, x-1):
        for b in range(1, x-a):
            c = n - a * b
            c //= a + b
            if c <= 0:
                break
            ans += min(c, x - a - b)
    print(str(ans) + '\n')
