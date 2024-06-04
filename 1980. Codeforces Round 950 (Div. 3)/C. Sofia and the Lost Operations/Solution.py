from collections import Counter
import sys

input = lambda: sys.stdin.readline().strip()
print = sys.stdout.write

t = int(input())

for _ in range(t):
    n = int(input())
    a = input().split()
    b = input().split()
    m = int(input())
    d = input().split()

    want = Counter()
    for i in range(n):
        j = b[i]
        if a[i] != j:
            want[j] += 1
    
    if d[-1] not in set(b):
        print('NO\n')
        continue
    for i in d:
        want[i] -= 1
    for i in want:
        if want[i] > 0:
            break
    else:
        print('YES\n')
        continue
    print('NO\n')
