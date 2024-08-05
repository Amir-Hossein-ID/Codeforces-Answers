import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    s = list(maput())
    odd = -1
    eve = []
    for i in s:
        if i % 2:
            odd = max(odd, i)
        else:
            eve.append(i)
    eve.sort()
    if len(eve) == 0 or odd == -1:
        print('0\n')
        continue
    i = 0
    ans = 0
    while i < len(eve):
        if eve[i] < odd:
            odd += eve[i]
            i += 1
        else:
            odd += eve[-1]
        ans += 1
    print(str(ans) + '\n')
