import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())
aa = 'aeiou'
for i in range(t):
    n = int(input())
    adds = n % 5
    for i in range(5):
        print(aa[i] * (n // 5))
        if adds:
            print(aa[i])
            adds -= 1
    print('\n')
