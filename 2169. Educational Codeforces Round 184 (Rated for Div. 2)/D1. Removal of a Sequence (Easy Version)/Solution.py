import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    x,y,k = maput()
    count = 1000000000000
    xx = x
    while xx and count >= y:
        count -= count // y
        xx -= 1
    if xx or count < k:
        print(-1)
        continue
    if k < y:
        print(k)
        continue
    while x:
        k += (k - 1) // (y-1)
        x -= 1
    print(k)
