import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n,m,q = maput()
    z = -1
    zz = -1
    st = m
    en = m
    ismiddle = False
    for qq in maput():
        if z != -1:
            if qq > z:
                z += 1
            if qq < zz:
                zz -= 1
        if qq >= st and qq <= en and z == -1:
            z = 1
            zz = n
        if qq < st and not ismiddle:
            st -= 1
        if qq > en and not ismiddle:
            en += 1
        ans = 0
        if st == en or ismiddle:
            if zz > z:
                ans = z + n - zz + 1
            else:
                ans = n
            ismiddle = True
        elif z != -1:
            if z >= st:
                ans += max(z, en)
            else:
                ans += z + en - st + 1
            if zz <= en:
                ans += n - max(z, en)
            else:
                ans += n - zz + 1
        else:
            ans += en - st + 1
        # print(st, en, z, zz)
        printf(str(ans) + ' ')
    printf('\n')
