import sys
    
input = sys.stdin.readline
print = sys.stdout.write
    
t = int(input())
    
for _ in range(t):
    n,m = map(int, input().split())
    table = []
    for i in range(n):
        table.append(input().strip())
    for i in range(n):
        ind = table[i].find('#')
        if ind != -1:
            y1 = i + 1
            x = ind + 1
            break
    for i in range(n - 1, -1, -1):
        ind = table[i].find('#')
        if ind != -1:
            y2 = i + 1
            break
    print(str((y1+y2)//2) + ' ' + str(x) + '\n')
