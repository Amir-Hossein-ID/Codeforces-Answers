import sys
import math
    
input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write
    
t = int(input())
    
for i in range(t):
    x,y,k = maput()
    aa = math.ceil(x/k)
    bb = math.ceil(y/k)
    ans = max(aa, bb) * 2 - int(aa > bb)
    print(str(ans) + '\n')
