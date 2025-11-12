import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

def do(x,y):
    if (x - y) % 2 == 0:
        printf('1 ')
    else:
        printf('0 ')

for i in range(t):
    a, b, c = maput()
    do(b, c)
    do(a, c)
    do(a, b)
    printf('\n')
