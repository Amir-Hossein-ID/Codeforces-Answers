import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n = int(input())
    print('mul 9')
    sys.stdout.flush()
    input()
    print('digit')
    sys.stdout.flush()
    input()
    print('digit')
    sys.stdout.flush()
    input()
    # always 9
    print(f'add {n-9}')
    sys.stdout.flush()
    input()
    print('!')
    sys.stdout.flush()
    input()
