import sys
    
input = sys.stdin.readline
print = sys.stdout.write

from collections import defaultdict
from heapq import heapify, heappop
    
t = int(input())
    
for _ in range(t):
    n = int(input())
    ns = [int(i) for i in input().split()]
    maps = defaultdict(list)
    for i in ns:
        maps[i - i%4].append(i)
    for i in maps:
        heapify(maps[i]) # using queue.PriorityQueue caused Memory Limit
    for i in ns:
        rem = heappop(maps[i - i%4])
        print(str(rem) + ' ')
    print('\n')
