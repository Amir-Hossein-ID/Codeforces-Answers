import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

n, q = maput()
dic = {i: 0 for i in range(51)}

for i,j in enumerate(maput()):
    if dic[j] == 0:
        dic[j] = i + 1

for t in maput():
    ans = dic[t]
    printf(str(ans) + ' ')
    for i in dic:
        if dic[i] < ans:
            dic[i] += 1
    dic[t] = 1
printf('\n')
