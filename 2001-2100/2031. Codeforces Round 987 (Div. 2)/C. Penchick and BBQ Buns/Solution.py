import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    n = int(input())
    if n == 1 or n == 3:
        print('-1\n')
        continue

    if n%2 == 0:
        i = 1
        while (i-1)*2 != n:
            print(f'{i} {i} ')
            i += 1
    elif n < 27:
        print('-1')
    else:
        print('1 2 2 3 3 4 4 5 5 1 ')
        print('6 6 7 7 8 8 9 9 10 10 11 11 13 12 12 1 13 ')
        i = 14
        while i*2 < n:
            print(f'{i} {i} ')
            i += 1
    print('\n')
