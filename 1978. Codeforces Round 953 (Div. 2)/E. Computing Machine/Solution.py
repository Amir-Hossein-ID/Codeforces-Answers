import sys
    
input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    q = int(input())
    canbeone = [False if i == '0' else True for i in a] # if ith index in "a" array can be one if we had no limits on the range 
    for i in (1, n-2):
        if i < n-1 and i > 0 and not canbeone[i]: #index 1 and n - 2 seprate from others to avoid these "i>0 and i < n-1" for others
            if b[i-1]=='1' and b[i+1]=='1':
                canbeone[i] = True
    for i in range(2, n-2):
        if not canbeone[i]:
            # if the before and after in "b" are 1 or can be 1 (via another 0 in a), so ith index can be 1
            if (b[i-1]=='1' or a[i-2] == '0') and (b[i+1]=='1' or a[i+2] == '0'):
                canbeone[i] = True
    
    sum = 0
    for i in range(n):
        sum += canbeone[i]
        canbeone[i] = sum

    for _ in range(q):
        l, r = maput()
        l-=1
        r-=1
        ans = int(a[l] == '1')
        if l < r:
            ans += a[r] == '1'
        added = False
        if l+1 < r:
            # if a[l+1] is 1 or can be 1 within the specified range
            ans += a[l+1] == '1' or (b[l] == '1' and (b[l+2]=='1' or (l+2 < r and a[l+3] == '0')))

        # r-1>l+1 because of avoiding duplicates (range length 3)
        if r-1 > l+1:
            ans += a[r-1] == '1' or (b[r] == '1' and (b[r-2]=='1' or a[r-3] == '0'))
        if r-l >= 4:
            ans += canbeone[r-2] - canbeone[l+1] 
        print(str(ans) + '\n')
