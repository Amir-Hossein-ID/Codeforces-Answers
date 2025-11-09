import sys

input = sys.stdin.readline
print = sys.stdout.write

t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    st = input().strip()
    i = n
    f = False
    wtf = st[i-1] # what to find :D
    while i >= 0:
        if st[i-k:i] == k * wtf:
            i -= k
            wtf = '1' if wtf == '0' else '0'
            f=True
        elif f:
            st = st[i:] + st[:i][::-1]
            break
        else:
            while st[i-1] == st[i-2]: i -= 1
            i -= 1
            wtf = st[i-1]
            f = True
    else:
        i = n
    if i == 0:
        i = n
    j = 0
    wtf = st[0]
    while j < n:
        if st[j:j+k] != k * wtf:
            break
        j += k
        wtf = '1' if wtf == '0' else '0'
    else:
        print(str(i)+'\n')
        continue
    print('-1\n')
