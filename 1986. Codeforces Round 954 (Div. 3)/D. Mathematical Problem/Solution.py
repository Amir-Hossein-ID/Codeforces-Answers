import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())
 
for _ in range(t):
    n = int(input())
    s = input()
    if n == 2:
        print(str(int(s)) + '\n')
        continue
    if '0' in s and (n > 3 or s[0]=='0' or s[-1] == '0'):
        print('0\n')
        continue

    tans = float('inf')

    for i in range(n-1):
        ans = int(s[i:i+2])
        for j in s[:i]:
            temp = int(j)
            if temp > 1:
                ans = ans + temp if ans > 1 else temp
        for j in s[i+2:]:
            temp = int(j)
            if temp > 1:
                ans = ans + temp if ans > 1 else temp
        tans = min(ans, tans)
    
    print(str(tans) + '\n')
