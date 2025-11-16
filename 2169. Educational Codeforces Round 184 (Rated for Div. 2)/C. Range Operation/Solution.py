import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    a = list(maput())
    pre = [0] * (n+1)
    s = 0
    for i, j in enumerate(a):
        s += j
        pre[i+1] = s

    # (r+l)(r-l+1) - (pre[r] - pre[l-1])
    # l - l^2 + pre[l-1]
    b = float('-inf')
    ans = 0
    for i in range(n):
        l = i + 1
        b = max(b, l - l * l + pre[l-1])

        ans = max(ans, b + l * (l + 1) - pre[l])

    print(ans + pre[-1])
