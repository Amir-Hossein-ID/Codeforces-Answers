import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

# t = int(input())

# for i in range(t):
s = input()
n = len(s)

i = (n+1) // 2 - 1
while i >= 0:
    if s[i:] == s[:-i]:
        print('YES\n')
        print(s[i:])
        break
    i -= 1
else:
    print('NO\n')
