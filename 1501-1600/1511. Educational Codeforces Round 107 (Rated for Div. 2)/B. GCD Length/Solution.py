import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for i in range(t):
    a, b, c = maput()
    gcd = 10 ** (c-1)
    a = 10 ** (a-1)
    b = 10 ** (b-1) + gcd
    print(a, b)
