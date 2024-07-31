import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    l1 = input()
    l2 = input()
    ans = 0
    f1 = l1.find('x.x')
    while f1 != -1:
        if l2[f1:f1+3] == '...': ans += 1
        f1 = l1.find('x.x', f1+1)
    f1 = l2.find('x.x')
    while f1 != -1:
        if l1[f1:f1+3] == '...': ans += 1
        f1 = l2.find('x.x', f1+1)
    print(str(ans) + '\n')
