import sys
    
input = sys.stdin.readline
print = sys.stdout.write
    
t = int(input())
    
for _ in range(t):
    s = input().strip()
    ans = 1
    last = s[0]
    f = False # has 01 in string
    for i in s[1:]:
        if i != last:
            ans += 1
            if not f and (i,last) == ('1', '0'):
                ans -= 1
                f = True
            last = i
    print(str(ans)+'\n')
