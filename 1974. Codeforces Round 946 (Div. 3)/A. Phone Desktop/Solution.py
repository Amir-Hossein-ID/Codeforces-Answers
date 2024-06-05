import math
t = int(input())

for i in range(t):
    n,m = map(int, input().split())
    ans = math.ceil(m / 2)
    n -= (m//2) * 7
    n -= (ans - m//2) * 4 + (ans - m//2) * 7
    if n <= 0:
        print(ans)
    else:
        print(ans + math.ceil(n / 15))
