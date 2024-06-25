import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n, l, r = maput()
    a = list(maput())
    ans = 0
    
    beg = 0
    en = 0
    sum_now = 0
    while en < n:
        sum_now += a[en]
        while sum_now > r:
            sum_now -= a[beg]
            beg += 1
        if sum_now >= l:
            ans += 1
            sum_now = 0
            beg = en + 1
        en += 1
    
    print(str(ans) + '\n')
