import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write


t = int(input())
for i in range(t):
    n = int(input())
    a = list(maput())

    biggest = 0
    cur = 0
    last = a[0]
    for i in a:
        if i == last:
            cur += 1
        else:
            last = i
            biggest = max(biggest, cur)
            cur = 1
    biggest = max(biggest, cur)

    print(str(n - biggest) + '\n')
