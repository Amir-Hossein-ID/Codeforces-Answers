import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    a = list(maput())
    b = list(maput())
    mi = 0 # -1 -1
    ma = 0 # 1 1
    f1 = 0
    f2 = 0
    for i in range(n):
        c,d = a[i], b[i]
        if c > d:
            f1 += c
        elif c < d:
            f2 += d
        elif c == d:
            if c == -1:
                mi += 1
            elif c == 1:
                ma += 1
    while mi:
        if f1 > f2:
            to = min(f1-f2, mi)
            f1 -= to
        elif f2 > f1:
            to = min(f2-f1, mi)
            f2 -= to
        else:
            f1 -= mi//2
            f2 -= mi//2
            if mi - mi//2*2:
                f1 -= 1
            to = mi
        mi -= to
    while ma:
        if f1 > f2:
            to = min(f1-f2, ma)
            f2 += to
        elif f2 > f1:
            to = min(f2-f1, ma)
            f1 += to
        else:
            f1 += ma//2
            f2 += ma//2
            if ma - ma//2*2:
                f1 += 1
            to = ma
        ma -= to
    print(str(min(f1, f2))+'\n')
