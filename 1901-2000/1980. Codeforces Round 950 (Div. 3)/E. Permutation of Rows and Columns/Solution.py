t= int(input())

for i in range(t):
    n,m = map(int, input().split())

    f = [[int(i) for i in input().split()] for i in range(n)]
    s = [[int(i) for i in input().split()] for i in range(n)]
    
    if n == 1 or m == 1:
        print('YES')
        continue

    mapp = []
    for i in f:
        for j in s:
            if i[0] in j:
                if set(i) == set(j):
                    mapp.append((i, j))
                    break
        else:
            print('NO')
            break
    else:
        for p in range(m):
            k = j.index(i[p])
            if k != -1:
                for tt, tj in mapp:
                    if tt[p] != tj[k]:
                        break
                else:
                    continue
                break
            else:
                break
        else:
            print('Yes')
            continue
        print('NO')
