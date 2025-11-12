import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for i in range(t):
    n = list(input())
    ind = len(n)-1
    num = ''
    zeros = ind + 1
    carry = False
    while ind >= 0:
        i = n[ind]
        if i > '4' or (carry and i > '3'):
            zeros = ind
            carry = True
        else:
            if carry:
                n[ind] = str(int(i) + 1)
            carry = False 
        ind -= 1
    if carry:
        printf('1')
    for i,j in enumerate(n):
        if i < zeros:
            printf(j)
        else:
            printf('0')
    printf('\n')
