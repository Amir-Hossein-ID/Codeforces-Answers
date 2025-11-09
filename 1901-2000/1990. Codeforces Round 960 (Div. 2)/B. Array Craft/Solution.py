import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n, x, y = maput()
    arr = [1] * n
    x -= 1
    y -= 1
    for i in range(x + 1, n, 2):
        arr[i] = -1
    for i in range(y - 1, -1, -2):
        arr[i] = -1
    for i in arr:
        print(str(i) + ' ')
    print('\n')
