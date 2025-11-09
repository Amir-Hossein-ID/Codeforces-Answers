import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())
mod = 998244353

from bisect import bisect_right

for _ in range(t):
    n,q = maput()
    a = list(maput())
    b = list(maput())

    asor = sorted(a)
    bsor = sorted(b)

    mul = 1
    for i in range(n):
        mul = (mul * min(asor[i], bsor[i])) % mod
    
    printf(str(mul) + ' ')

    for i in range(q):
        o, x = maput()
        if o == 1:
            tochange = a[x-1]
            ind = bisect_right(asor, tochange)
            if bsor[ind-1] > tochange:
                mul = (mul * pow(tochange, -1, mod)) % mod # calculates inverse modulo like pow(tochange, mod-2, mod)) from fermet little
                mul = (mul * (tochange + 1)) % mod
            asor[ind-1] += 1
            a[x-1] += 1
        else:
            tochange = b[x-1]
            ind = bisect_right(bsor, tochange)
            if asor[ind-1] > tochange:
                mul = (mul * pow(tochange, -1, mod)) % mod
                mul = (mul * (tochange + 1)) % mod
            bsor[ind-1] += 1
            b[x-1] += 1

        printf(str(mul) + ' ')
    
    printf('\n')
