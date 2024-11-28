import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write


t = int(input())
for i in range(t):
    a = input()
    b = input()
    ans = len(a) + len(b)
    did = False
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            ans -= 1
            did = True
        else:
            break
    if did: ans += 1
    print(str(ans) + '\n')
