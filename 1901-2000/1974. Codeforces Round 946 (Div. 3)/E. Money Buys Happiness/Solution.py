import sys

input = sys.stdin.readline
print = sys.stdout.write

t = int(input())

for i in range(t):
    m,x = map(int, input().split())

    f = [[int(i) for i in input().split()] for i in range(m)]
    
    dp = {0: 0}
    max_ = 0

    for i in range(m):
        cost = f[i][0]
        happ = f[i][1]
        new_dp = {i:dp[i] for i in dp}
        for j in dp:
            if dp[j] + cost <= i * x:
                new_dp[happ + j] = min(new_dp.get(happ + j, float('inf')), dp[j] + cost)
                max_ = max(max_, happ + j)
        dp = new_dp
    print(str(max_) + '\n')
