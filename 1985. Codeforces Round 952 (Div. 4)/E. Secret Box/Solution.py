import sys

input = sys.stdin.readline
print = sys.stdout.write

t = int(input())

for _ in range(t):
    x,y,z,k = map(int, input().strip().split())
    ans = 0
    for i in range(x,0,-1):
        for j in range(y, 0, -1):
            p = k // i // j
            if p > z:
                break
            c = i*j*p
            if c == k:
                ans = max(ans, (x-i+1) * (y-j+1) * (z-p+1))
    print(str(ans) + '\n')
