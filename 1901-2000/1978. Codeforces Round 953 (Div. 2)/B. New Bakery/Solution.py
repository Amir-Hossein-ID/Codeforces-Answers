t = int(input())

for i in range(t):
    n, a, b = map(int, input().split())
    if b <= a:
        print(n*a)
        continue
    ans = 0
    high = b
    low = max(b-min(n, b), a)

    ans = high * (high + 1) - low * (low + 1)
    ans //= 2
    n -= (high - low)
    n = max(0, n)
    print(ans + n*a)
