import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    l,r = maput()
    s = bin(r)[2:]
    p = bin(l)[2:].rjust(len(s), '0')

    ind = 0
    for i in range(len(s)):
        ind = i
        if s[i] != p[i]:
            break
    # ind2 = len(s) -1
    # while p[ind2] == '1':
    #     ind2 -= 1
    while True:
        ss = ''
        for j in range(len(s)):
            if j < ind:
                ss += s[j]
            else:
                ss += '1' if s[j] == '0' else '0'
        ss = int(ss, 2)
        if ss >= l and ss <= r:
            break
        ind += 1
    pp = 0
    for i in range(l,r):
        if i != ss:
            pp = i
            break
    printf(str(r) + " " + str(ss) + " " + str(pp) + '\n')
