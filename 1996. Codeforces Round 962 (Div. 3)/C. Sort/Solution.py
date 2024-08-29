import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n,q = maput()
    a = input()
    b = input()
    acount = [0] * 26
    bcount = [0] * 26
    acounts = [acount]
    bcounts = [bcount]
    queries = []

    for i in range(n):
        acount = acount.copy()
        bcount = bcount.copy()

        acount[ord(a[i]) - 97] += 1
        bcount[ord(b[i]) - 97] += 1

        acounts.append(acount)
        bcounts.append(bcount)
    for i in range(q):
        i, j = maput()
        ans = 0
        for p in range(26):
            ans += max(bcounts[j][p] - bcounts[i-1][p] - (acounts[j][p] - acounts[i-1][p]), 0)
        print(str(ans) + '\n')
