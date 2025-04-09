import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

from collections import Counter

for _ in range(t):
    n = int(input())
    a = Counter(maput())

    num = 1
    while num < n+1:
        if a[num] >= 2:
            a[num+1] += a[num] - 2
        elif a[num] == 1:
            break
        num += 1
    else:
        print("YES")
        continue
    print("NO")
