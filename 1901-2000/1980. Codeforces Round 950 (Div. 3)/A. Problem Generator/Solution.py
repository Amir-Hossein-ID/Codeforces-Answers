t = int(input())
    
for i in range(t):
    n,m = map(int, input().split())
    s = input()
    ans = 0
    for i in 'ABCDEFG':
        ans += max(m - s.count(i), 0)
    print(ans)
