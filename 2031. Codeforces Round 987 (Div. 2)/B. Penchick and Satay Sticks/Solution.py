import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    a = list(maput())
    for i in range(1, n+1):
        if abs(a[i-1] - i) > 1:
            print("NO\n")
            break
    else:
        print('YES\n')
