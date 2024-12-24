import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n,k = maput()
    a = list(maput())
    b = list(maput())
    aa = sorted(range(n), key=lambda x: a[x])
    bb = sorted(range(n), key=lambda x: b[x])

    where_a = 0
    where_b = 0
    ans = 0
    while True:
        if where_a - where_b <= k:
            ans = max(ans, a[aa[where_a]] * (n - where_b))
        before = a[aa[where_a]]
        while where_a < n and a[aa[where_a]] == before:
            where_a += 1
        if where_a == n:
            break
        while where_b < n and a[aa[where_a]] > b[bb[where_b]]:
            where_b += 1
    
    where_a = 0
    where_b = 0
    while where_a < n and b[bb[where_b]] > a[aa[where_a]]:
        where_a += 1
    
    while True:
        if where_a - where_b <= k:
            ans = max(ans, b[bb[where_b]] * (n - where_b))
        before = b[bb[where_b]]
        while where_b < n and b[bb[where_b]] == before:
            where_b += 1
        if where_b == n:
            break
        while where_a < n and b[bb[where_b]] > a[aa[where_a]]:
            where_a += 1
    
    printf(str(ans) + '\n')
