t = int(input())

for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = a.copy()

    last = 0
    while last < n:
        if a[last] != -1:
            last = last
            break
        last += 1
    else:
        for i in range(n):
            print(i % 2 + 1, end = ' ')
        print()
        continue

    for i in range(last, 0, -1):
        if ans[i] == 1:
            ans[i - 1] = 2
        else:
            ans[i - 1] = ans[i] // 2
    i = last + 1

    while i < n:
        if a[i] != -1:
            left = last
            right = i
            while left < right - 1:
                if ans[left] > ans[right]:
                    left += 1
                    ans[left] = ans[left - 1] // 2
                elif ans[right] != 1:
                    right -= 1
                    ans[right] = ans[right + 1] // 2
                else:
                    right -= 1
                    ans[right] = 2
            last = i
        i += 1

    while last < n - 1:
        if ans[last] == 1:
            ans[last + 1] = 2
        else:
            ans[last + 1] = ans[last] // 2
        last += 1

    for i in range(n - 1):
        if ans[i] // 2 != ans[i+1] and ans[i+1] // 2 != ans[i]:
            break
    else: 
        print(*[abs(i) for i in ans], sep=' ')
        continue
    print(-1)
