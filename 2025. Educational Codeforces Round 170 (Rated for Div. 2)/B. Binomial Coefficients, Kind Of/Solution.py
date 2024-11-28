import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

# t = int(input())

# for i in range(t):
n = int(input())
maput()


for i in maput():
    print(str(pow(2, i, 1000000007)) + '\n')
