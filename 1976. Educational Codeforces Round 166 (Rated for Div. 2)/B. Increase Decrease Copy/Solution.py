t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    add = b[-1]

    ans = 1
    mindis = abs(a[0] - add)
    for i in range(n):
        ans += abs(a[i] - b[i])
        if (a[i] >= add and b[i] <= add) or (a[i] <= add and b[i] >= add):
            mindis = 0
        mindis = min(mindis, abs(b[i] - add), abs(a[i] - add))
    print(ans + mindis)
