import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    ans = min(s.count('A'), n) + min(s.count('B'), n) + min(s.count('C'), n) + min(s.count('D'), n)
    print(str(ans) + '\n')
