import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

import re

for i in range(t):
    n = int(input())
    a = input()
    a = re.sub('0+', '0', a)
    print('YES\n' if a.count('0') < a.count('1') else 'NO\n')
