import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

n = int(input())

dic = {}

for i, j in enumerate(maput()):
    dic[i+2] = j

path = [n]
cur = n
while cur != 1:
    new = dic[cur]
    path.append(new)
    cur = new

for i in path[::-1]:
    printf(str(i) + " ")
printf('\n')
