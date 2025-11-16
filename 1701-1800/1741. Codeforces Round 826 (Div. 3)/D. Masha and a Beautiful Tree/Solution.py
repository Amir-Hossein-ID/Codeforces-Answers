import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n = int(input())
    p = list(maput())
    j = 1
    ans = 0
    while j < n:
        for i in range(0, n, j*2):
            a,b = p[i], p[i+j]
            if a > b:
                p[i] = b
                ans += 1
            if abs(a-b) != j:
                print(-1)
                break
        else:
            j *= 2
            continue
        break
    else:
        print(ans)
        continue
