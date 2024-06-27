import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    a,b = input(), input()
    ans = len(a)
    blen = len(b)
    best = 0
    for i in range(blen):
        cur_ans = 0
        pos = 0
        ind = a.find(b[i], pos)
        while ind != -1:
            i += 1
            pos = ind+1
            cur_ans += 1
            if i < blen:
                ind = a.find(b[i], pos)
            else:
                break
        best = max(best, cur_ans)
    print(str(ans + blen - best)+'\n')
