t = int(input())

for i in range(t):
    x, y = map(int, input().split())

    ans = 0

    while x != 0 or y != 0:
        if x % 2 == y % 2:
            ans += 1
        else:
            break
        x //= 2
        y //= 2
    
    print(2**ans)
