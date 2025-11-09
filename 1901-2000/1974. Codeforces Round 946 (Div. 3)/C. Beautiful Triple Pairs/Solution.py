from collections import Counter

t = int(input())

for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]

    pairs = Counter()
    fpairs = Counter()
    for i in range(n-2):
        pairs[(a[i], a[i+1], 0)] += 1
        pairs[(a[i], 0, a[i+2])] += 1
        pairs[(0, a[i+1], a[i+2])] += 1
        fpairs[(a[i], a[i+1], a[i+2])] += 1
    
    ans = 0
    for i in pairs:
        ans += pairs[i] * (pairs[i] - 1) // 2
    for i in fpairs:
        ans -= (fpairs[i] * (fpairs[i] - 1) // 2) * 3

    print(ans)
