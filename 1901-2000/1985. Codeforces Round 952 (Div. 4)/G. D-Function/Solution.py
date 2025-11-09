import sys
    
input = sys.stdin.readline
print = sys.stdout.write
    
t = int(input())
    
for _ in range(t):
    l,r,k = map(int, input().split())
    a = 1
    for i in range(1, 10):
        if i*k < 10:
            a += 1

    ans = pow(a, l, 1000000007)
    ans *= pow(a, r - l, 1000000007) - 1
    ans %= 1000000007

    print(str(ans) + '\n')
