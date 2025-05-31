import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    s = input()
    op = 0
    ans = -1
    for i in s:
        if i == '(':
            op += 1
        elif i == ')':
            op -= 1
        if op == 0:
            ans += 1
    if ans == 0:
        print('NO')
    else:
        print("YES")
