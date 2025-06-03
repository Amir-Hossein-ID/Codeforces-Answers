import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())
MOD  =998244353

for _ in range(t):
    n = int(input())
    p = list(maput())
    q = list(maput())
    maxp = p[0]
    maxpi = 0
    maxq = q[0]
    maxqi = 0
    print((pow(2, p[0], MOD) + pow(2, q[0], MOD)) % MOD, end=" ")

    for i in range(1, n):
        if p[i] > maxp:
            maxp = p[i]
            maxpi = i
        if q[i] > maxq:
            maxq = q[i]
            maxqi = i
        if maxp > maxq:
            print((pow(2, maxp, MOD) + pow(2, q[i-maxpi], MOD)) % MOD, end=" ")
        elif maxq > maxp:
            print((pow(2, p[i-maxqi], MOD) + pow(2, maxq, MOD)) % MOD, end=" ")
        elif q[i-maxpi] > p[i-maxqi]:
            print((pow(2, maxp, MOD) + pow(2, q[i-maxpi], MOD)) % MOD, end=" ")
        else:
            print((pow(2, p[i-maxqi], MOD) + pow(2, maxq, MOD)) % MOD, end=" ")
