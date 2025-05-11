import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(maput())
    ans = 0
    last = -1
    aa = []
    for i in a:
        if i != last:
            aa.append(i)
            last = i
    n = len(aa)
    b = sorted(range(n), key=lambda i: aa[i], reverse=True)
    pressed = [False] * n
    for i in b:
        pressed[i] = True
        if not((i > 0 and pressed[i-1]) or (i < n-1 and pressed[i+1])):
            ans += 1
    print(ans)
