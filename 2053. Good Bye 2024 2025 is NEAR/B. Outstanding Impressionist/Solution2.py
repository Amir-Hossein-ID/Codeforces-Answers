import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n = int(input())
    num = 2*n+1
    cant = [0] * num
    a = []
    for i in range(n):
        b,c = maput()
        a.append((b,c))
        if b==c:
            cant[b] += 1
    prefix = [0] * num
    for i in range(1, num):
        prefix[i] = prefix[i-1] + (cant[i] != 0)

    for i in a:
        if i[0] == i[1]:
            printf('1' if cant[i[0]] < 2 else '0')
        else:
            printf('1' if prefix[i[1]] - prefix[i[0] - 1] < i[1] - i[0] + 1 else '0')
    printf('\n')
