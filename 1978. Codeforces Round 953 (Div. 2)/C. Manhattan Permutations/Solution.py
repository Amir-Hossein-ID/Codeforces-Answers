import sys
    
input = sys.stdin.readline
print = sys.stdout.write

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    if k % 2:
        print('NO\n')
        continue
    if k == 0:
        print('YES\n')
        for i in range(1, n+1):
            print(str(i)+' ')
        print('\n')
        continue
    nums = list(range(1, n+1))
    ans = nums.copy()
    s = 0
    e = n - 1
    while s < e:
        cal = abs(nums[s] - ans[e]) * 2
        if cal <= k:
            k -= cal
            ans[s], ans[e] = ans[e], ans[s]
            s += 1
            e -= 1
            continue
        s += 1
    if k == 0:
        print('YES\n')
        for i in ans:
            print(str(i)+' ')
        print('\n')
    else:
        print('NO\n')
