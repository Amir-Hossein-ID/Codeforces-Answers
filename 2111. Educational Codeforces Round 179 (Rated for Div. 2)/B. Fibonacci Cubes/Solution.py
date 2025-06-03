import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())
cu = [1,2,3,5,8,13,21,34,55,89,144]

for _ in range(t):
    n, m = maput()
    for i in range(m):
        newn = n
        size = list(maput())
        while newn > 0:
            size.sort()
            if any([i < cu[newn-1] for i in size]):
                print('0', end='')
                break
            size[-1] -= cu[newn-1]
            newn -= 1
        else:
            print('1', end='')
    print()
