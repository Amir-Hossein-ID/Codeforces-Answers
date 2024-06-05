import sys

input = sys.stdin.readline
print = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    m = input().strip()
    no = we = ea = so = 0
    for i in m:
        if i == 'N':
            no += 1
        elif i == 'E':
            ea += 1
        elif i == 'S':
            so += 1
        else:
            we += 1

    if abs(no-so) % 2 == 0 and abs(we-ea) % 2 == 0:
        ans = ''
        he = max((ea-we) // 2, 0)
        hw = max((we-ea) // 2, 0)
        hn = max((no-so) // 2, 0)
        hs = max((so-no) // 2, 0)
        if (he, hw, hn, hs) == (0,0,0,0):
            if no > 1 or (we > 0 and no > 0):
                hn += 1
                hs += 1
            elif we > 1 or (no > 0 and we > 0):
                hw += 1
                he += 1
            else:
                print('NO\n')
                continue
        m = m.replace('N', 'H', hn)
        m = m.replace('W', 'H', hw)
        m = m.replace('S', 'H', hs)
        m = m.replace('E', 'H', he)
        for i in m:
            if i == 'H':
                print(i)
            else:
                print('R')
        print('\n')
    else:
        print('NO\n')
