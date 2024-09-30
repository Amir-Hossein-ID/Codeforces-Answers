import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n,k = maput()
    a = list(maput())
    mx = max(a)
    s = sum(a)
    
    ans = min(n, (k+s) // mx)
    while True:
        if s % ans == 0:
            break

        nxt = s - s % ans + ans
        if k + s >= nxt:
            break
        ans -= 1

    print(str(ans) + '\n')
