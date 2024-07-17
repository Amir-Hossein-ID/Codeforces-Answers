import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    ans = []
    i = 0
    while 2 ** i <= n:
        x = (1 << i)
        if n & x and n != x:
            ans.append(n - x)
        i += 1
    print(str(len(ans) + 1) + '\n')
    for i in ans[::-1]:
        print(str(i) + ' ')
    print(str(n) + '\n')
