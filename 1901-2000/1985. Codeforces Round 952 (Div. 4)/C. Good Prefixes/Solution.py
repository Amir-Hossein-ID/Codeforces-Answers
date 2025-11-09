t = int(input())

for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    sum_ = 0
    max_ = a[0]
    ans = 0
    for i in a:
        sum_ += i
        max_ = max(max_, i)
        if sum_ == max_ * 2:
            ans += 1
    print(ans)        
