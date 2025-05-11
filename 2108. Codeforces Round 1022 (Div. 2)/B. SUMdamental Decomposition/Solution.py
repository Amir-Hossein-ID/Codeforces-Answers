import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

from collections import defaultdict

for _ in range(t):
    n,x = maput()
    xbin = bin(x)[2:] 
    zero = max(0, n - xbin.count('1'))
    ans = 0
    pow = 1
    pows = defaultdict(int)
    if n == 1 and x == 0:
        print(-1)
        continue
    for i in xbin[::-1]:
        if i == '1':
            pows[pow] += 1
            ans += pow

        todo = min((zero+1)//2*2, n - pows[pow])
        if todo % 2 == 1:
            todo -= 1
        # print(todo, (zero+1)//2*2,  n - pows[pow])
        ans += todo * pow
        zero -= todo
        pows[pow] += todo
        pow *= 2
        # print(ans,pow//2)
    if zero == 0:
        print(ans)
    else:
        todo = min((zero+1)//2*2, n - pows[pow])
        if todo % 2 == 1:
            todo -= 1
        ans += todo * pow
        zero -= todo
        pows[pow] += todo
        print(ans)
