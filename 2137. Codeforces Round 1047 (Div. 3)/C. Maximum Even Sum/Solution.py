import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    a,b = maput()
    ans = -1
    if a % 2 == 0 and b % 2 == 1:
        print(-1)
        continue
    if a % 2 == 1 and b % 2 == 0:
        if b % 4 == 0:
            ans = 2 + a * b//2
    elif a % 2 == 1 and b % 2 == 1:
        ans = 1 + a * b
    else:
        ans = 2 + a * b //2
    
    print(ans)
