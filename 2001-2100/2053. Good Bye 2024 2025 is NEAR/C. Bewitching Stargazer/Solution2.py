import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n,k = maput()
    ans = n+1
    seg = 1
    cseg = 0
    
    while n >= k:
        if n%2:
            cseg += seg
        seg *= 2
        n//=2
    
    printf(str(cseg//2*(ans) + ((ans)//2 if ans % 2 == 0 else 0)) + '\n')
