import sys
    
input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

for _ in range(t):
    n, m, k = maput()
    table = []
    for i in range(n):
        table.append(list(maput()))
    snowy = []
    for i in range(n):
        snowy.append([True if j =='0' else False for j in input()])
    
    snowy_sum = [[0] * m for i in range(n)]
    to_achieve = 0
    for i in range(n):
        row_sum = 0
        for j in range(m):
            row_sum += snowy[i][j]
            snowy_sum[i][j] = row_sum + (snowy_sum[i-1][j] if i > 0 else 0)
            if snowy[i][j]:
                to_achieve += table[i][j]
            else:
                to_achieve -= table[i][j]

    to_achieve = abs(to_achieve)
    lowest_can_do = 0
    if to_achieve != 0:
        for i in range(n-k+1):
            for j in range(m-k+1):
                sn = snowy_sum[i+k-1][j+k-1]
                if i > 0:
                    sn -= snowy_sum[i-1][j+k-1]
                    if j > 0:
                        sn += snowy_sum[i-1][j-1]
                if j > 0:
                    sn -= snowy_sum[i+k-1][j-1]
                ns = k * k - sn
                lowest_can_do = gcd(lowest_can_do, abs(ns-sn))
        if lowest_can_do and to_achieve % lowest_can_do == 0:
            print('YES\n')
        else:
            print('NO\n')
    else:
        print('YES\n')
