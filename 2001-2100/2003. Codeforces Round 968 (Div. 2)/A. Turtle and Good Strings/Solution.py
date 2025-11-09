import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    if s[0] != s[-1]:
        print('YES\n')
    else:
        print('NO\n')
