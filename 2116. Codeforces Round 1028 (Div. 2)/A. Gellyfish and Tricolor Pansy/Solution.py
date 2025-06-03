import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())


for i in range(t):
    a,b,c,d = maput()
    if (a >= d and c >= d) or (a >= b and c >= b):
        print('Gellyfish')
    else:
        print('Flower')
