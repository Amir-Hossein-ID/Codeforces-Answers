import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    b,c,d = maput()
    ans = b - c
    b = bin(b)[2:]
    c = bin(c)[2:]
    d = bin(d)[2:]
    maxlen = max(len(b), len(c), len(d))
    b = b.rjust(maxlen, '0')
    c = c.rjust(maxlen, '0')
    d = d.rjust(maxlen, '0')
    a = 0
    
    for e, i, j, k in zip(range(len(b) - 1, -1, -1), b, c, d):
        if i == '0':
            if j == '0' and k == '1':
                a += 2 ** e
            elif k == '1':
                a = None
                break
        else:
            if j == '0'and k == '0':
                a = None
                break
            elif j == '1' and k == '0':
                a += 2 ** e
    
    if a != None:
        print(str(a) + '\n')
    else:
        print('-1\n')
