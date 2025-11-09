import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n,m = maput()
    arr = []
    for i in range(n):
        a = list(maput())
        arr.append(a[1:] + a[0:1])
    arr = arr[1:] + arr[0:1]
    if n*m == 1:
        print('-1\n')
        continue
    for i in arr:
        for j in i:
            print(str(j) + ' ')
        print('\n')
