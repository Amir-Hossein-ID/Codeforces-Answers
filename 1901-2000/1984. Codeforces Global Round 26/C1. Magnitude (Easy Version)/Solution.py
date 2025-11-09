t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mi = 0
    ma = 0
    for i in a:
        mi, ma = mi + i, max(abs(ma + i), abs(mi + i))
    print(ma)
