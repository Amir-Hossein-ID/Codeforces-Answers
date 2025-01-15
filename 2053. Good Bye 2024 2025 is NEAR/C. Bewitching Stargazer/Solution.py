import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())
def do(n,k):
    if n < k:
        return 0,0
    if n==1:
        return 1,1
    if n % 2:
        a,b = do(n//2, k)
        return a + (n // 2 + 1) + a + (n//2 + 1) * b, b*2 + 1
    else:
        a,b= do(n//2, k) 
        return a + a + (n//2) * b, b*2

for _ in range(t):
    n,k = maput()
    ans = 0
    seg = 1

    if k == 1:
        printf(str(n * (n+1)//2) + '\n')
    else:
        printf(str(do(n,k)[0]) + '\n')
