import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n,q = maput()
    s = input()
    inds = {'ba':0, 'ca':0, 'cb':0, 'bc':0, 'bca':0, 'cba':0}
    for i in range(q):
        a,b = input().split()
        if a == 'a' or a == b:
            continue
        if a == 'b':
            if b == 'c':
                inds['bc'] += 1
            elif inds['cb']:
                inds['cb'] -= 1
                inds['cba'] += 1
            else:
                inds['ba'] += 1
        elif a == 'c':
            if b == 'b':
                inds['cb'] += 1
            elif inds['bc']:
                inds['bc'] -= 1
                inds['bca'] += 1
            else:
                inds['ca'] += 1

    news = list(s)
    for i,j in enumerate(s):
        if j == 'b':
            if inds['ba']:
                inds['ba'] -= 1
                news[i] = 'a'
            elif inds['cba']:
                inds['cba'] -= 1
                inds['cb'] += 1
                news[i] = 'a'
            elif inds['bca']:
                inds['bca'] -= 1
                news[i] = 'a'
        elif j == 'c':
            if inds['ca']:
                inds['ca'] -= 1
                news[i] = 'a'
            elif inds['bca']:
                inds['bca'] -= 1
                news[i] = 'a'
            elif inds['cba']:
                inds['cba'] -= 1
                news[i] = 'a'
            elif inds['cb']:
                inds['cb'] -= 1
                news[i] = 'b'
    print(''.join(news))
