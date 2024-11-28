import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write


t = int(input())
for i in range(t):
    n = int(input())
    a = list(maput())
    b = sorted(a)
    ans = [0] * n

    sum_is = 0
    sum_should = 0

    best_ans = b[-1]

    for i in range(n-1, -1, -1):
        sum_should += b[i]
        sum_is += a[i]
        if sum_is != sum_should:
            ans[i] = best_ans
        else:
            ans[i] = best_ans
            best_ans = b[i-1]
            sum_should = 0
            sum_is = 0
    
    for i in ans:
        printf(str(i) + ' ')
    printf('\n')
