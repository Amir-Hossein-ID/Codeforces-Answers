import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

from collections import Counter

for i in range(t):
    n = int(input())
    s = input()
    s = Counter(s)
    c = 0
    while c != n:
        for i in s:
            if s[i]:
                print(i)
                s[i] -= 1
                c += 1
    
    print('\n')
