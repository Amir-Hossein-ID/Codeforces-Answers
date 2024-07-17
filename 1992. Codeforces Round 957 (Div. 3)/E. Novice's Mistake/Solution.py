import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for _ in range(t):
    sn = input()
    n = int(sn)
    oops = (sn*7)[:7]
    to_check = [int(oops[:i]) for i in range(1, 8)]
    ans = []
    for a in range(1, 10001):
        mul = n * a
        maxb = min(10000, mul)
        for i in range(len(to_check)):
            to = to_check[i]
            ll = i + 1
            b = mul - to
            if b > 0 and b < maxb and len(sn) * a - ll == b:
                ans.append((a,b))
    print(str(len(ans)) + '\n')
    for i in ans:
        print(str(i[0]) + ' ' + str(i[1]) + '\n')
