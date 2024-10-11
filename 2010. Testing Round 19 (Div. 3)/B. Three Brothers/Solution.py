import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

# t = int(input())

# for i in range(t):
k = set(maput())
print(str(6 - sum(k)))
