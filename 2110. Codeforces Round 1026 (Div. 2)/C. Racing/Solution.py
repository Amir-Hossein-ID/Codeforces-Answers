import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n = int(input())
    d = list(maput())
    hs = []
    for i in range(n):
        hs.append(tuple(maput()))
    cur_height = 0
    uppers = [0] * n
    cans = []
    can_go_upper = 0
    for i, j in enumerate(d):
        if j == 1:
            cur_height += 1
        elif j == -1:
            can_go_upper += 1
            cans.append(i)
            d[i] = 0
        uppers[i] = can_go_upper
        if cur_height >= hs[i][0]:
            if cur_height <= hs[i][1]:
                can_go_upper = min(can_go_upper, hs[i][1] - cur_height)
            else:
                break
        elif cur_height + can_go_upper >= hs[i][0]:
            while cur_height < hs[i][0] and can_go_upper > 0:
                can_go_upper -= 1
                d[cans.pop()] = 1
                cur_height += 1
            can_go_upper -= hs[i][0] - cur_height
            cur_height = hs[i][0]
            can_go_upper = min(can_go_upper, hs[i][1] - cur_height)
        else:
            break            
    else:
        print(*d)
        continue
    print(-1)
