t = int(input())

for i in range(t):
    a,b,c,d = [int(i) for i in input().split()]
    a,b = min(a,b), max(a,b)
    c,d = min(c,d), max(c,d)
    if c > a and c < b and d > b:
        print('YES')
    elif a > c and a < d and b > d:
        print('YES')
    else:
        print('NO')
