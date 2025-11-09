import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    op = [0]
    opc = 1
    clc = 0
    ans = 0
    for i in range(1,n,2):
        if s[i] == '(':
            op.append(i)
            opc += 1
        else:
            ans += i - op.pop()
            clc += 1
        if opc > clc:
            clc += 1
            ans += i + 1 - op.pop()
        else:
            opc += 1
            op.append(i+1)
    print(str(ans) + '\n')
