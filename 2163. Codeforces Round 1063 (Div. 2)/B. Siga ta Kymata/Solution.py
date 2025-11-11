import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    p = list(maput())
    s = input()
    mind = p.index(1)
    mand = p.index(n)
    if s[0] == '1' or s[-1] == '1':
        print(-1)
        continue
    if s[mind] == '1' or s[mand] == '1':
        print(-1)
        continue
    mind, mand = min(mind, mand), max(mind, mand)
    print(5)
    print(1, mind+1)
    print(1, mand+1)
    print(mind + 1, n)
    print(mand + 1, n)
    print(mind + 1, mand + 1)
    