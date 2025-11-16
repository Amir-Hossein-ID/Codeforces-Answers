import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    s = input()
    ans = 0
    last = ''
    dp = [0] * (len(s) + 1)
    for i, j in enumerate(s):
        if (last == '>' and (j == '*' or j == '<')) or \
            (last == '*' and (j == '*' or j == '<')):
            print(-1)
            break
        if j == '<':
            dp[i+1] = dp[i] + 1
        elif j == '*':
            dp[i+1] = dp[i] + 1
        last = j
    else:
        ans = max(dp)
        dp = [0] * (len(s) + 1)
        for i in range(len(s)-1, -1, -1):
            if s[i] == '>':
                dp[i] = dp[i+1] + 1
            elif s[i] == '*':
                dp[i] = dp[i+1] + 1
        print(max(max(dp), ans))
