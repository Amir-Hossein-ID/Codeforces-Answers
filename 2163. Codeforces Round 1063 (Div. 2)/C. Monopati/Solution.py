import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    fr = list(maput())
    sr = list(maput())
    fmi = [fr[0]] * n
    fma = [fr[0]] * n
    mi = fr[0]
    ma = fr[0]
    for i, j in enumerate(fr):
        if j > ma:
            ma = j
        elif j < mi:
            mi = j
        fmi[i] = mi
        fma[i] = ma
    smi = [0] * n
    sma = [0] * n
    mi = fr[0]
    ma = fr[0]
    for i, j in enumerate(sr[::-1]):
        if j > ma:
            ma = j
        elif j < mi:
            mi = j
        smi[-i-1] = mi
        sma[-i-1] = ma

    do = [2*n+1] * (2*n+1)
    for i in range(n):
        allmi = min(fmi[i], smi[i])
        allma = max(fma[i], sma[i])
        do[allmi] = min(do[allmi], allma)

    for i in range(2*n-1, 0, -1):
        do[i] = min(do[i], do[i+1])

    # ans = 0
    # for i in do:
    #     ans += 2 * n - i + 1
    ans = (2*n+1)*(2*n+1) - sum(do)
    print(ans)
