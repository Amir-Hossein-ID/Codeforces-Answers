import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    x,y,k = maput()
    while x >= y and k:
        rem = y - x % y
        if rem <= k:
            x += rem
            while x % y == 0: x //= y
            k -= rem
        else:
            x += k
            k = 0
    if k:
        print(str((k+x-1) % (y-1) + 1) + '\n')
    else:
        print(str(x) + '\n')
