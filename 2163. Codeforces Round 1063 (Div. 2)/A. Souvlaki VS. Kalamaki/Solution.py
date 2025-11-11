import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    a = sorted(maput())
    for i in range(1, n-1, 2):
        if a[i] != a[i+1]:
            print('NO')
            break
    else:
        print("YES")
