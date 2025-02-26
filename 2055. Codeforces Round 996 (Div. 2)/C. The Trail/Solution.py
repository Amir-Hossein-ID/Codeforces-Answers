import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n,m = maput()
    s = input()
    table = [list(maput()) for i in range(n)]
    my_val = 0
    where_i = 0
    where_j = 0
    where_s = 0
    if s[0] == 'D':
        for i in range(m):
            my_val += table[0][i]
        where_i += 1
    else:
        for i in range(n):
            my_val += table[i][0]
        where_j += 1
    table[0][0] = -my_val
    
    for j in s[1:]:
        if j == 'D':
            sumi = 0
            for i in range(m):
                sumi -= table[where_i][i]
            table[where_i][where_j] = sumi
            where_i += 1
        else:
            sumi = 0
            for i in range(n):
                sumi -= table[i][where_j]
            table[where_i][where_j] = sumi
            where_j += 1
    
    sumi = 0
    for i in range(m):
        sumi -= table[-1][i]
    table[where_i][where_j] = sumi
    
    for i in table:
        for j in i:
            printf(str(j) + ' ')
        printf('\n')
