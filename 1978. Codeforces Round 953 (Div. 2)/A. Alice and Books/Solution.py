t = int(input())

for i in range(t):
    n = int(input())
    m = list(map(int, input().split()))
    print(max(m[:-1]) + m[-1])
