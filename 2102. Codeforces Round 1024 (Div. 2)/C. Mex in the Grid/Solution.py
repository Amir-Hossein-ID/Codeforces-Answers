import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n = int(input())
    table = [[0] * n for i in range(n)]
    row = (n-1)//2
    col = (n-1)//2
    count = 1
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dcount = 1
    dnum = 0
    table[row][col] = 0
    while count < n*n:
        for i in range(2):
            for i in range(dcount):
                if count == n*n:
                    break
                row += d[dnum][0]
                col += d[dnum][1]
                if row < 0 or row >= n or col < 0 or col >= n:
                    break
                table[row][col] = count
                count += 1
            dnum = (dnum + 1) % 4
        dcount += 1
    for i in range(n):
        for j in range(n):
            printf(str(table[i][j]) + ' ')
        printf('\n')
