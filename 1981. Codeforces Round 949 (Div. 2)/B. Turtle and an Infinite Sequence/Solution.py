t = int(input())

for i in range(t):
    n, m = [int(i) for i in input().split()]
    if m == 0:
        print(n)
        continue
    ans = n
    ans |= max(0, n - m)
    ans |= n + m
    ans |= int('1' * len(bin(m)[2:]), 2)
    print(ans)
