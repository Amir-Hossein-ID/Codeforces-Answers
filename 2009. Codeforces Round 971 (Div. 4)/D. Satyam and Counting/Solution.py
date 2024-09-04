import sys
    
input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

from collections import defaultdict

for _ in range(t):
    n = int(input())
    ans = 0
    p1 = defaultdict(list)
    for i in range(n):
        a,b = maput()
        p1[a].append(b)
    for b in p1:
        c = p1[b]
        ans += (n - 2) * (len(c) - 1)
        for i in c:
            if (b+1 in p1 and (not i) in p1[b+1]) and (b-1 in p1 and (not i) in p1[b-1]):
                ans += 1
    print(str(ans) + '\n')
