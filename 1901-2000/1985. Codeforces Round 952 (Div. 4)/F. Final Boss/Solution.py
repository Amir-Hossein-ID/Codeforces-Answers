from queue import PriorityQueue
import heapq
import sys
    
input = sys.stdin.readline
print = sys.stdout.write
    
t = int(input())
    
for _ in range(t):
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    curc = [(c[i]+1, i) for i in range(n)]
    heapq.heapify(curc)
    ss = sum(a)
    h -= ss
    ans = 1
    while h > 0:
        newt, i = heapq.heappop(curc)
        ans = newt
        h -= a[i]
        heapq.heappush(curc, (ans + c[i], i))
    print(str(ans) + '\n')
