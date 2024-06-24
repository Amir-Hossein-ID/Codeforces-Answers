import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n, m = maput()
    s = list(input())
    ind = sorted(list(set(maput())))
    c = sorted(input())

    for i,j in enumerate(ind):
        s[j-1] = c[i]
    print(''.join(s)+'\n')
