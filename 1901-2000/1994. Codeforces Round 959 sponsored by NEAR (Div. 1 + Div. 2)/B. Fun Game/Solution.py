import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    t = input()
    imp = False
    for i in range(n):
        # every thing after first one can be changed, so only before it matters
        # for example for (0 -> 1) we manage to xor the 0 with the 1 
        # and for (1 -> 1) we xor it with itself to become 0
        # but we can not do them in indexes before the first one
        if s[i] == '1':
            break
        if s[i] != t[i]:
            imp = True
            break
    if imp:
        print('NO\n')
    else:
        print('YES\n')
