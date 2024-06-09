t = int(input())

for i in range(t):
    n = int(input())
    x = input().split()
    if x[0] != x[-1]:
        print('YES')
        print('RB' + 'R'*(n-2))
    else:
        print('NO')
