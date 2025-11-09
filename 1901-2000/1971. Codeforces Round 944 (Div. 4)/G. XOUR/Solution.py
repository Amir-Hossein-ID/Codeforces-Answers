import sys
    
input = sys.stdin.readline
print = sys.stdout.write
    
from collections import defaultdict
    
t = int(input())
    
for _ in range(t):
    n = int(input())
    ns = [int(i) for i in input().split()]
    maps = defaultdict(list)
    ind = defaultdict(int)
    for i in ns:
        maps[i - i%4].append(i) # i - i%4 was too much faster than i >> 2 (shift)
    for i in maps:
        maps[i] = sorted(maps[i])
    for i in ns:
        rem4 = i - i%4
        rem = maps[rem4][ind[rem4]]
        ind[rem4] += 1
        print(str(rem) + ' ')
    print('\n')
