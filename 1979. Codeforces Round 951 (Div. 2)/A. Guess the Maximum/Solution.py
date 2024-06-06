t = int(input())

for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]

    min_max = float('inf')

    for i in range(n-1):
        t = max(a[i], a[i+1])
        min_max = min(min_max, t)

    print(min_max - 1)
