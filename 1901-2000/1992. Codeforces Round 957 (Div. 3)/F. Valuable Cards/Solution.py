import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write
    
t = int(input())

for _ in range(t):
    n, x = maput()
    a = list(maput())
    ans = 1
    needs = set()
    for i in a:
        if i in needs:
            ans += 1
            needs = set()
        to_add = set()
        for j in needs:
            if j % i == 0:
                to_add.add(j//i)
        if x % i == 0:
            to_add.add(x//i)
        needs.update(to_add)
    print(str(ans) + '\n')
