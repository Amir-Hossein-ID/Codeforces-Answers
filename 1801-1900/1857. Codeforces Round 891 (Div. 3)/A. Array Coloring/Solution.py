import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for i in range(t):
    n = list(input())
    if sum(i%2 for i in maput()) % 2 == 0:
        print('YES')
    else:
        print("NO")
