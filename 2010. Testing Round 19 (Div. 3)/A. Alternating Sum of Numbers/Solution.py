import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write


t = int(input())
for i in range(t):
    n = int(input())
    a = list(maput())
    ans = 0
    for i in range(n):
        ans += (-1 if i % 2 else 1) * a[i]
    print(str(ans) + '\n')
