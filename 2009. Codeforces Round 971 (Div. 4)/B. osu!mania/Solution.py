import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    a = [input().find('#') + 1 for i in range(n)]
    for i in a[::-1]:
        print(str(i) + ' ')
    print('\n')
