import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n,m = maput()
    mat = []
    for i in range(n):
        mat.append(list(maput()))
    
    for i in range(n):
        for j in range(m):
            cur = mat[i][j]
            ma = 0
            if i > 0:
                if mat[i-1][j] >= cur:
                    continue
                ma = max(ma, mat[i-1][j])
            if i < n-1:
                if mat[i+1][j] >= cur:
                    continue
                ma = max(ma, mat[i+1][j])
            if j > 0:
                if mat[i][j-1] >= cur:
                    continue
                ma = max(ma, mat[i][j-1])
            if j < m-1:
                if mat[i][j+1] >= cur:
                    continue
                ma = max(ma, mat[i][j+1])
            mat[i][j] = ma
    for i in range(n):
        printf(*mat[i])

