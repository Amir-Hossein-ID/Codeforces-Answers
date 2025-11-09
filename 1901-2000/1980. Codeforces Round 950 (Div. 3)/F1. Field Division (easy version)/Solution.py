import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write
    
t = int(input())

for _ in range(t):
    n, m, k = maput()
    fountains = []
    for _ in range(k):
        fountains.append(tuple(maput()))
    f_sort_ind = sorted(range(k), key=lambda x: (fountains[x][1], fountains[x][0]))
    f_sort_y = [fountains[i] for i in f_sort_ind]
    anslist = [0 for i in range(k)]
    i = 0
    curm = 1
    lowest = 0
    ans = 0
    while True:
        s_before = lowest
        changed = 0
        while i < k and f_sort_y[i][1] == curm:
            lowest = max(lowest, f_sort_y[i][0])
            changed = i
            i += 1
        if changed < k and s_before != lowest:
            anslist[f_sort_ind[changed]] = 1
        if i < k:
            ans += (f_sort_y[i][1] - curm) * (n - lowest)
        else:
            ans += (m - curm + 1) * (n - lowest)
            break
        curm = f_sort_y[i][1]

    print(str(ans) + '\n')
    for i in anslist:
        print(str(i) + ' ')
    print('\n')
