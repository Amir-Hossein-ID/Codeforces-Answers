import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

def do(s):
    ans = s.count('X')
    if s[-1] == 'S':
        return -1 - ans
    elif s[-1] == 'L':
        return 1 + ans
    else:
        return 0

for _ in range(t):
    a, b = input().split()
    a, b = do(a), do(b)
    if a > b:
        print('>')
    elif b > a:
        print('<')
    else:
        print('=')
