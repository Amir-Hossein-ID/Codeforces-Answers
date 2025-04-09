import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())
for _ in range(t):
    s = input()
    print(s.count('1'))
