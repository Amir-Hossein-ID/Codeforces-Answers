import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n = int(input())
    print('digit')
    sys.stdout.flush()
    input()
    print('digit')
    sys.stdout.flush()
    input()
    print('add -8')
    sys.stdout.flush()
    input()
    print('add -4')
    sys.stdout.flush()
    input()
    print('add -2')
    sys.stdout.flush()
    input()
    print('add -1')
    sys.stdout.flush()
    input()
    print('mul', n)
    sys.stdout.flush()
    input()
    print('!')
    sys.stdout.flush()
    input()
