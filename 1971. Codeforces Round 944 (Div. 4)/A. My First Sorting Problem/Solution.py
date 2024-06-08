t = int(input())

for i in range(t):
    x = [int(i) for i in input().split()]
    print(min(x), max(x))
