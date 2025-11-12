import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    if '...' in s:
        print(2)
    else:
        print(s.count('.'))
