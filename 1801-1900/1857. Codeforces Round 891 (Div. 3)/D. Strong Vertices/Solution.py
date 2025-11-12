import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    a = list(maput())
    b = list(maput())
    asort = sorted(range(n), key=lambda x: (a[x]-b[x], -x), reverse=True)
    ans = []
    last = a[asort[0]] - b[asort[0]]
    for i in asort:
        cur = a[i] - b[i]
        if cur == last:
            ans.append(i+1)
        else:
            break
    print(len(ans))
    print(*ans)
