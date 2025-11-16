import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

from bisect import bisect_left

for _ in range(t):
    n = int(input())
    p = list(maput())
    pre = [0] * n
    s = 0
    for i, j in enumerate(p):
        s += j
        pre[i] = s
    
    ans = n

    for end in range(n):
        sum = pre[end]
        cur_sum = pre[end]
        cur_ind = end
        cur_max = end + 1
        while True:
            cur_sum += sum
            ind = bisect_left(pre, cur_sum)
            if ind < n and pre[ind] == cur_sum:
                cur_max = max(cur_max, ind - end)
                end = ind
                if ind == n-1:
                    break
            else:
                cur_max = float('inf')
                break
        ans = min(cur_max, ans)
    
    print(ans)
