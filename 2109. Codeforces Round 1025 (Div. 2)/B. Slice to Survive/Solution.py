import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n,m,a,b = maput()
    aans = float('inf')
    cuts = [(n-(n-a+1)), (n-a), (m-(m-b+1)), (m-b)]

    for cut in cuts[:2]:
        newn = n-cut
        newm = m
        ans = 1
        while newn !=1:
            newn = (newn+1)//2
            ans += 1
        while newm !=1:
            newm = (newm+1)//2
            ans += 1
        aans = min(ans, aans)

    for cut in cuts[2:]:
        newn = n
        newm = m-cut
        ans = 1
        while newn !=1:
            newn = (newn+1)//2
            ans += 1
        while newm !=1:
            newm = (newm+1)//2
            ans += 1
        aans = min(ans, aans)
    
    print(aans)
