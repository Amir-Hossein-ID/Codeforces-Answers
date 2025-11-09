import sys
    
input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for _ in range(t):
    n, k = maput()
    low = k
    high = k + n - 1
    ans = float('inf')
    while low <= high:
        mid = (low + high) // 2
        half1 = (k + mid - 1) * (mid - k) // 2
        half2 = (mid + k + n - 1) * (k + n - mid) // 2
        ans = min(ans, abs(half1 - half2))
        if half1 == half2:
            break
        elif half1 > half2:
            high = mid - 1
        else:
            low = mid + 1
    print(str(ans) + '\n')
