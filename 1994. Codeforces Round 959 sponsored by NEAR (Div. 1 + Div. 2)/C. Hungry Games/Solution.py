import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

from bisect import bisect_left

for i in range(t):
    n, x = maput()
    a = list(maput())
    prsum = []
    s = 0
    for i in a:
        s += i
        prsum.append(s)
    
    goods = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        j = bisect_left(prsum, prsum[i] - a[i] + x + 1)
        if j == n:
            goods[i] = n - i
        else:
            goods[i] = goods[j + 1] + j - i
    print(str(sum(goods)) + '\n')
