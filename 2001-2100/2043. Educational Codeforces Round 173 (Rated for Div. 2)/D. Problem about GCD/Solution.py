import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for _ in range(t):
    l,r,g = maput()
    l += g - l % g if l % g else 0
    r -= r % g
    ll = l //g
    rr = r//g

    best = (0,0)
    max = -1
    while gcd(ll, rr) != 1:
        newrr = rr
        while gcd(ll, newrr) != 1:
            newrr -= 1
            if ll > newrr:
                break
        else:
            if newrr - ll > max:
                max = newrr - ll
                best = (ll, newrr)
            ll += 1
            continue
        break
    else:
        if rr - ll > max:
            max = rr - ll
            best = (ll, rr)
    if max!=-1:    
        printf(str(best[0] * g) + ' ' + str(best[1] * g) + '\n')
    else:
        printf("-1 -1\n")
