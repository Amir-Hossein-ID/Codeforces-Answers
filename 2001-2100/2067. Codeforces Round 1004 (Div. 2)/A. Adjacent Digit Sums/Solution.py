import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())
for _ in range(t):
    x,y = maput()
    if (x > y and (x - y + 1) % 9 == 0) or x == y - 1:
        print('YES')
    else:
        print("NO")
