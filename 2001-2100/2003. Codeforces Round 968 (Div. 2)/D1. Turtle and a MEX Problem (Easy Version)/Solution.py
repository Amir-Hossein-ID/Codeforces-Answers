import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n, m = maput()
    ans = 0
    for i in range(n):
        a = list(maput())
        l = a[0]
        visited = [0] * (l + 2)
        for i in a[1:]:
            if i < l + 2:
                visited[i] = 1
        best = 0
        while visited[best]:
            best += 1
        best += 1
        while visited[best]:
            best += 1
        ans = max(best, ans)
    
    mul = 0 if m < ans else 1
    temp = m * (m + 1) // 2 - ans * (ans - 1) // 2
    ans = ans * min(ans, m + 1) + temp * mul
    ans = int(ans)
    print(str(ans) + '\n')
