import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())


for i in range(t):
    n = int(input())
    a = list(maput())

    a.sort()
    if (a[0] + a[n-1]) % 2 == 0:
        print(0)
    else:
        min1 = 0
        ans = 0
        while min1 < n:
            if (a[min1] ^ a[0]) % 2 != 1:
                ans += 1
                min1 += 1
                continue
            break
        max = n-1
        ans2 = 0
        while max >= 0:
            if (a[max] ^ a[n-1]) % 2 != 1:
                ans2 += 1
                max -= 1
                continue
            break
        print(min(ans, ans2))
