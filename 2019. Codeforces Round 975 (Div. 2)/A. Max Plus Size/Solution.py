import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())
for i in range(t):
    n = int(input())
    a = list(maput())
    if n == 1:
        print(str(1+a[0]) + '\n')
        continue
    ans = max(max(a[::2]) + (n+1) // 2, max(a[1::2]) + n//2)
    print(str(ans) +'\n')
