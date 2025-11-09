import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n,k,l = maput()
    a = list(maput())
    ans = a[0]
    x = k
    cur_a = 0
    
    while x < l:
        if cur_a != n-1:
            if a[cur_a+1] < x:
                cur_a += 1
                a[cur_a] = min(a[cur_a] + ans, x)
                x = a[cur_a] + k
            elif a[cur_a+1] == x:
                cur_a += 1
                x = a[cur_a] + k
            elif a[cur_a+1] - ans <= x:
                cur_a += 1
                a[cur_a] = x
                x += k
            else:
                ansb = ans
                ans += (a[cur_a+1] - ans - x) / 2
                cur_a += 1
                a[cur_a] = (a[cur_a] - ansb - x) / 2 + x
                x = a[cur_a] + k
        else:
            ans += l - x
            x = l
    printf(str(int(ans*2))+'\n')
