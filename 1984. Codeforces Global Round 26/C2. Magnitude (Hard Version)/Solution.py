t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mi = 0
    ma = 0
    reach = {0:1}
    for i in a:
        mi, ma = mi + i, max(abs(ma + i), abs(mi + i))
        newr = {}
        for j in reach:
            temp = i + j
            if temp == mi or temp == ma:
                newr[temp] = (newr.get(temp, 0) + reach[j]) % 998244353
            temp = abs(temp)
            if temp == mi or temp == ma:
                newr[temp] = (newr.get(temp, 0) + reach[j]) % 998244353
        reach = newr
    print(reach[ma] % 998244353)
