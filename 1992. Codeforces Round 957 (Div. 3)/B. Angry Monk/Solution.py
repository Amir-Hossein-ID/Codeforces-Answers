import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n,k = maput()
    a = list(maput())
    ma = a[0]
    ans = 0
    for i in range(k):
        ss = a[i]
        if ss >= ma:
            ma = ss
        ans += ss + ss - 1
    ans -= ma + ma - 1
    print(str(ans)+'\n')
