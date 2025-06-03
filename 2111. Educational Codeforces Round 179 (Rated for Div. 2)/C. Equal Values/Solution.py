import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(maput())
    last = a[0]
    last_ind = 0
    ans = float('inf')
    for i,j in enumerate(a):
        if j != last:
            nans = last * last_ind + (n - i) * last
            ans = min(nans, ans)
            last = j
            last_ind = i
    nans = last * last_ind
    ans = min(nans, ans)
    print(ans)
