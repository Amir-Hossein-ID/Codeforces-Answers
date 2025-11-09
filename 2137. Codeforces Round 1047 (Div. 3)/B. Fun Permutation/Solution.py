import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    for i in maput():
        print(n - i + 1, end = ' ')
    print()
