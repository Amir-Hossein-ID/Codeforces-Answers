import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n, m = maput()
    s = input()
    ind = list(maput())
    c = sorted(input())
    ind.sort()

    beg = 0
    ans = ''
    lastind = 0
    for i in ind:
        if i != lastind+1:
            ans += s[lastind:i-1]
        if i == lastind:
            continue
        ans += c[beg]
        beg += 1
        lastind = i
    if lastind != n:
        ans += s[lastind:]
    print(ans+'\n')
