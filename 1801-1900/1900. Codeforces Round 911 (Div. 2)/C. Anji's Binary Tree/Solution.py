import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

def closest():
    best_ans = float('inf')
    todo = [(1,0)]
    while todo:
        cur, changes = todo.pop()
        if cur == 0:
            continue
        child = childs[cur-1]
        if child == (0,0):
            best_ans = min(changes, best_ans)
            continue
        todo.append((child[0], changes + (s[cur-1] != 'L')))
        todo.append((child[1], changes + (s[cur-1] != 'R')))
    return best_ans

for i in range(t):
    n = int(input())
    s = input()
    childs = [(0,0) for i in range(n)]
    parents = [0] * (n+1)
    cur = 1
    for i in range(n):
        inp = tuple(maput())
        childs[i] = inp
        parents[inp[0]] = i+1
        parents[inp[1]] = i+1
    print(closest())


