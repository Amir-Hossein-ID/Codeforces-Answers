import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(maput())

    num_ind = -1

    f_res = 0
    f_max = 0
    f_res2 = 0
    f_min = 0

    s_res = -2
    s_max = -2
    s_res2 = 2
    s_min = 2

    i = 0
    while i < n:
        if abs(a[i]) == 1:
            f_max = max(f_max + a[i], a[i])
            f_res = max(f_res, f_max)
            f_min = min(f_min + a[i], a[i])
            f_res2 = min(f_res2, f_min)
        else:
            num_ind = i
            break
        i += 1
    
    i += 1
    while i < n:
        s_max = max(s_max + a[i], a[i])
        s_res = max(s_res, s_max)
        s_min = min(s_min + a[i], a[i])
        s_res2 = min(s_res2, s_min)
        i += 1
    
    if num_ind == -1:
        printf(str(f_res - f_res2 + 1) + '\n')
        for i in range(f_res2, f_res + 1):
            printf(str(i) + ' ')
        printf('\n')
    else:
        max_after = a[num_ind]
        min_after = max_after
        c1 = max_after
        max_before = max_after
        min_before = max_after
        c2= max_after

        i = num_ind + 1
        while i < n:
            c1 += a[i]
            max_after = max(max_after, c1)
            min_after = min(min_after, c1)
            i += 1
        i = num_ind - 1
        while i >= 0:
            c2 += a[i]
            max_before = max(max_before, c2)
            min_before = min(min_before, c2)
            i -= 1
        
        # print(max_after, min_after, max_before, min_before)
        ans = set(range(f_res2, f_res + 1)).union(set(range(s_res2, s_res + 1))).union(\
            set(range(min_before + min_after - a[num_ind], max_after + max_before - a[num_ind] + 1)))

        printf(str(len(ans)) + '\n')
        for i in sorted(ans):
            printf(str(i) + ' ')
        printf('\n')
