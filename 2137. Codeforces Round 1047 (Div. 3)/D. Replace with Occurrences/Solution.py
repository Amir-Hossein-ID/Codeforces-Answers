import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n = int(input())
    b = list(maput())
    ans = []
    a = [0] * (n+1)
    ins = [0] * (n+1)
    cur = 1
    for i in b:
        if a[i] > 0:
            a[i] -= 1
            ans.append(ins[i])
        else:
            ans.append(cur)
            ins[i] = cur
            a[i] = i-1
            cur += 1
    if any(i > 0 for i in a) or cur > n+1:
        print(-1)
    else:
        for i in ans:
            print(i, end= ' ')
        print()
