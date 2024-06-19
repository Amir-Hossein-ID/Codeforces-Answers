import sys
from collections import defaultdict
    
input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

def calconn(start: list):
    ans = 0
    new_group = len(group_counts)
    while start:
        togo = start.pop()
        i = togo[0]
        j = togo[1]
        if groups[i][j]:
            continue
        ans += 1
        groups[i][j] = new_group
        if i > 0 and table[i - 1][j] == '#':
            start.append((i-1, j))
        if i < n - 1 and table[i + 1][j] == '#':
            start.append((i+1, j))
        if j < m - 1 and table[i][j + 1] == '#':
            start.append((i, j+1))
        if j > 0 and table[i][j - 1] == '#':
            start.append((i, j-1))
    group_counts.append(ans)

t = int(input())

for _ in range(t):
    n, m = maput()
    table = []
    for i in range(n):
        table.append(input())
    groups = [[0 for i in range(m)] for j in range(n)]
    group_counts = [0]

    for i in range(n):
        for j in range(m):
            if table[i][j] == '#' and groups[i][j] == 0:
                calconn([(i,j)])

    maxans = 0
    for i in range(n):
        ans = 0
        add_groups = set()
        for j in range(m):
            add_groups.add(groups[i][j])
            if table[i][j] == '.':
                ans += 1
            if i > 0:
                add_groups.add(groups[i-1][j])
            if i < n - 1:
                add_groups.add(groups[i+1][j])
        ans += sum(group_counts[i] for i in add_groups)
        maxans = max(ans, maxans)

    for j in range(m):
        ans = 0
        add_groups = set()
        for i in range(n):
            add_groups.add(groups[i][j])
            if table[i][j] == '.':
                ans += 1
            if j > 0:
                add_groups.add(groups[i][j-1])
            if j < m - 1:
                add_groups.add(groups[i][j+1])
        ans += sum(group_counts[i] for i in add_groups)
        maxans = max(ans, maxans)
    
    print(str(maxans) + '\n')
